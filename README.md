# kubectl-lsdeploy
## Summary
Plugin for kubectl written in Python. 
Queries the kubernetes API and prints an overview of
- namespaces
- deployment
- replica sets
- pods
- nodes

Based on [Issue #72794](https://github.com/kubernetes/kubernetes/issues/72794) I didn't find a built-in function.

Mostly PEP-8 compliant but otherwise "way to go" when it comes to code quality.

### References
[Kubernetes Core V1 API](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md)
[Kubernetes APP V1 API](https://github.com/kubernetes-client/go/blob/master/kubernetes/docs/AppsV1beta2Api.md)


## Installation

Clone the repo and install the requirements:
```bash
git clone https://github.com/dominikzorgnotti/kubectl-lsdeploy
cd kubectl-lsdeploy
pip3 install -r requirements.txt
```
Move the main script to an place that is in your path, e.g.:
```bash
mv kubectl-lsdeploy.py /usr/local/bin
```
Verify that kubectl recognizes the plugin
```bash
kubectl plugin list
```



### Tested with
  - Python 3.8.0 on Windows 10 (see Issues)
  - Python 3.5.2 on Ubuntu 16.04.06 LTS (x64)
  - Python modules:
    - kubernetes: 10.0.1
    - PrettyTable: 0.7.2
  - Kubernetes:
    - 1.17 
    - 1.16

## Usage
Once in your path can run the script directly with

```bash
kubectl-lsdeploy.py
```
or as subcommand of kubectl
```bash
kubectl lsdeploy.py
```

### Example output
```
+----------------------+---------------------------+--------------------------------------+--------------------------------------------+-----------------+
|      Namespace       |         Deployment        |              ReplicaSet              |                    Pod                     |   Hosting node  |
+----------------------+---------------------------+--------------------------------------+--------------------------------------------+-----------------+
|       default        |            demo           |           demo-7cbf698c44            |           demo-7cbf698c44-6z68g            | 192.168.113.131 |
|       default        |           demo2           |           demo2-5657dc98db           |           demo2-5657dc98db-4jwbk           | 192.168.113.131 |
|     kube-system      |          coredns          |          coredns-6955765f44          |          coredns-6955765f44-bp7zl          | 192.168.113.131 |
|     kube-system      |          coredns          |          coredns-6955765f44          |          coredns-6955765f44-k4swp          | 192.168.113.131 |
|     kube-system      |          coredns          |          coredns-6955765f44          |               etcd-minikube                | 192.168.113.131 |
|     kube-system      |          coredns          |          coredns-6955765f44          |        kube-addon-manager-minikube         | 192.168.113.131 |
|     kube-system      |          coredns          |          coredns-6955765f44          |          kube-apiserver-minikube           | 192.168.113.131 |
|     kube-system      |          coredns          |          coredns-6955765f44          |      kube-controller-manager-minikube      | 192.168.113.131 |
|     kube-system      |          coredns          |          coredns-6955765f44          |              kube-proxy-mzzd7              | 192.168.113.131 |
|     kube-system      |          coredns          |          coredns-6955765f44          |          kube-scheduler-minikube           | 192.168.113.131 |
|     kube-system      |          coredns          |          coredns-6955765f44          |            storage-provisioner             | 192.168.113.131 |
| kubernetes-dashboard | dashboard-metrics-scraper | dashboard-metrics-scraper-7b64584c5c | dashboard-metrics-scraper-7b64584c5c-6nxks | 192.168.113.131 |
| kubernetes-dashboard |    kubernetes-dashboard   |    kubernetes-dashboard-79d9cd965    |    kubernetes-dashboard-79d9cd965-fj6lj    | 192.168.113.131 |
+----------------------+---------------------------+--------------------------------------+--------------------------------------------+-----------------+
```


