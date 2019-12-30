#!/usr/bin/env python3
import kubernetes
from prettytable import PrettyTable
import argparse
import json
import yaml

"""
Author: Dominik Zorgnotti (@dominikzorgnotti)
Version: 1.1
Summary: Print aggregated information about the dependencies of deployments and pods

Import modules:
kubernetes -> Kubernetes Python client libraries: get all the required information
prettytable -> pretty table to create nice output
argparse -> read arguments from the command line
json, yaml -> output format 
"""
__version__ = "1.1"

""" Prepare to hold our command line arguments in the variable args """
parser = argparse.ArgumentParser(allow_abbrev=False, description="Print aggregated information about the dependencies of deployments and pods")
version = "%(prog)s " + __version__
parser.add_argument("--version", "-v", action="version", version=version)
parser.add_argument("-o", "--output", 
                choices=["table", "json", "yaml"],
                default="table", type=str, help="Output format: table (default), json or yaml")
args = parser.parse_args()

def QueryKubernetesApi(KubernetesClient):
    """ Query the Kubernetes API and return the results as dict """
    KubernetesApiResult = {}
    KubernetesApiResult["AppsV1Api"] = kubernetes.client.AppsV1Api(kubernetes.client.ApiClient(KubernetesClient))
    KubernetesApiResult["CoreV1Api"] = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(KubernetesClient))
    return KubernetesApiResult

def GetAllInfo(KubernetesApiInput):
    """ Take the Input from the Kubernetes API and aggregate it """
    """ From Replicasets and Pods we can gather all the info we need """    
    GetAllReplicaSets =  KubernetesApiInput["AppsV1Api"].list_replica_set_for_all_namespaces(watch=False)
    GetAllPods = KubernetesApiInput["CoreV1Api"].list_pod_for_all_namespaces(watch=False)
    # Create an empty list that holds our dicts with the information
    PodList = list()
    """ Iterate through all pods and store the info about the name of the pod, NameSpace, Replicaset and Node"""
    for MyPodItems in GetAllPods.items:
        if (MyPodItems.metadata.owner_references) and (MyPodItems.metadata.owner_references[0].kind == "ReplicaSet"):
            MyPodReplicaSet = MyPodItems.metadata.owner_references[0].name
        PodList.append({"PodName": MyPodItems.metadata.name, "PodNameSpace": MyPodItems.metadata.namespace,
                        "PodReplicaSet": MyPodReplicaSet, "PodHostingNode": MyPodItems.status.host_ip})

    """ Iterate through all Replicasets and match these to the pods. From the replicaset we supply the deployment info to the dict """
    for MyReplicaItems in GetAllReplicaSets.items:
        for MyPod in PodList:
            if MyPod["PodReplicaSet"] == MyReplicaItems.metadata.name:
                MyPod.update(
                    {"PodDeployment": MyReplicaItems.metadata.owner_references[0].name})
    return PodList

def OutputAsTable (ProcessedApiResults):
    """Print table based on the provided list with deployment information"""
    OutputTable = PrettyTable()
    OutputTable.field_names = ["Namespace",
                               "Deployment", "ReplicaSet", "Pod", "Hosting node"]
    for MyPodInfo in ProcessedApiResults:
        OutputTable.add_row([MyPodInfo["PodNameSpace"], MyPodInfo["PodDeployment"],
                         MyPodInfo["PodReplicaSet"], MyPodInfo["PodName"], MyPodInfo["PodHostingNode"]])
    print(OutputTable)

def OutputAsYaml (ProcessedApiResults):
    """return yaml based on the provided list with deployment information"""
    print("Return as YAML not implemented yet")

def OutputAsJson (ProcessedApiResults):
    """return json based on the provided list with deployment information"""
    print("Return as JSON not implemented yet")

def main(output):
    """ initialise K8s client """
    kubernetes.config.load_kube_config()
    GetKubernetesConfiguration = kubernetes.client.Configuration()
    """ Retrieve information from API """
    KubernetesApi =  QueryKubernetesApi(GetKubernetesConfiguration)
    """ Go through the API info and build the output """
    DeploymentInfo = GetAllInfo(KubernetesApi)
    if output == "table":
        OutputAsTable(DeploymentInfo)
    elif output == "yaml":
        OutputAsYaml(DeploymentInfo)
    elif output == "json":
        OutputAsJson(DeploymentInfo)


main(**vars(args))  

## return values from functions
