# kubectl-lsdeploy
## Summary
Plugin for kubectl written in Python. 
Queries the kubernetes API and prints an overview of
- namespaces
- deployment
- replica sets
- pods
- nodes

Mostly PEP-8 compliant but otherwise "way to go" when it comes to code quality.

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

## Usage
Once in your path can run the script directly with

```bash
kubectl-lsdeploy.py
```
or as subcommand of kubectl
```bash
kubectl lsdeploy.py
```

## Tested with
  - Python 3.8.0 on Windows 10 (see Issues)
  - Python 3.5.2 on Ubuntu 16.04.06 LTS (x64)
  - Python modules:
    - kubernetes: 10.0.1
    - PrettyTable: 0.7.2
  - Kubernetes:
    - 1.17 
    - 1.16
