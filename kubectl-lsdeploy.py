#!/usr/bin/env python3
import kubernetes
from prettytable import PrettyTable

"""
Author: Dominik Zorgnotti (@dominikzorgnotti)
Version: 1.0
Summary: Print aggregated information about the dependencies of deployments and pods

Import modules:
kubernetes -> Kubernetes Python client libraries: get all the required information
prettytable -> and pretty table to create nice output"""

""" Create an empty list that holds our dicts with the information """
Podlist = list()

""" Configs can be set in Configuration class directly or using helper utility """
kubernetes.config.load_kube_config()
GetK8sConfiguration = kubernetes.client.Configuration()
GetV1ApiApps = kubernetes.client.AppsV1Api(
    kubernetes.client.ApiClient(GetK8sConfiguration))
GetV1ApiCore = kubernetes.client.CoreV1Api(
    kubernetes.client.ApiClient(GetK8sConfiguration))

""" From Replicasets and Pods we can gather all the info we need """
GetAllReplicaSets = GetV1ApiApps.list_replica_set_for_all_namespaces(
    watch=False)
GetAllPods = GetV1ApiCore.list_pod_for_all_namespaces(watch=False)

""" Iterate through all pods and store the info about the name of the pod, NameSpace, Replicaset and Node"""
for MyPodItems in GetAllPods.items:
    if (MyPodItems.metadata.owner_references) and (MyPodItems.metadata.owner_references[0].kind == "ReplicaSet"):
        MyPodReplicaSet = MyPodItems.metadata.owner_references[0].name

    Podlist.append({"PodName": MyPodItems.metadata.name, "PodNameSpace": MyPodItems.metadata.namespace,
                    "PodReplicaSet": MyPodReplicaSet, "PodHostingNode": MyPodItems.status.host_ip})

""" Iterate through all Replicasets and match these to the pods. From the replicaset we supply the deployment info to the dict """
for MyReplicaItems in GetAllReplicaSets.items:
    for MyPod in Podlist:
        if MyPod["PodReplicaSet"] == MyReplicaItems.metadata.name:
            MyPod.update(
                {"PodDeployment": MyReplicaItems.metadata.owner_references[0].name})

"""Print table based on the provided list with deployment information"""
OutputTable = PrettyTable()
OutputTable.field_names = ["Namespace",
                               "Deployment", "ReplicaSet", "Pod", "Hosting node"]
for MyPodInfo in Podlist:
    OutputTable.add_row([MyPodInfo["PodNameSpace"], MyPodInfo["PodDeployment"],
                         MyPodInfo["PodReplicaSet"], MyPodInfo["PodName"], MyPodInfo["PodHostingNode"]])
print(OutputTable)
