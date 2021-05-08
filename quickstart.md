Honey-clusters (/ˈklʌstə ˈhʌni/)

Sandboxing untrustes 

These are the yaml files, scripts and code for my bachelor's dissertation/thesis and will no longer be maintained beyond: May 2021.

Honeypots are intentionally exposed networks, systems or applications. One can study the attacks made on honeypots in order to get real time data about what exploits are being used.

Masking a honeypot as a decoy application can often lead to better results due 

Features:

  - gVisor Kernel Isolation of each Honeypot instance in a Honey-cluster
  - Cowrie as base docker image [Cowrie](https://github.com/cowrie/cowrie)
  - works in Google Kubernetes Engine (GKE) | [Documentation](https://cloud.google.com/kubernetes-engine) [Quickstart](https://cloud.google.com/kubernetes-engine/docs/quickstart) 
  - run dozens of self-healing honeypots on a single VPS/Dedicated Instance
  - deploy into any existing cluster
  - incl. simple decoy Cryptocurrency Price Api [FastApi Homepage](https://fastapi.tiangolo.com/)
  - 

To Do:

- Auto-Scaling
- ELK / Greylog / Graphana
- Istio (or any Service Mesh)
- Alpine Linux - Destruct Images after 1h
- eBPF Cilium https://github.com/cilium/cilium


 The idea is that one lets attackers a cybersecurity 

# Deploying 2 Nodes (1 decoy, 1 honeypot)

Because container runtimes like docker, container-d, OCI, OCR and CRI-O share the kernel between containers, when misconfigured or run as root (default) they are vulnerable to container breakouts and many other container vulnerabilities. This is especially important to consider when we run un-trusted workloads like honeypots.

In order to further create a sandbox around attackers we can isolate containers against a range of kernel exploits using a tool like gVisor ([Github](https://github.com/google/gvisor)). 

Alternatives include:
- OpenStack katacontainers [katacontainers.io](https://katacontainers.io/)
- AWS-Firecracker [Github](https://github.com/firecracker-microvm/firecracker), [Kubernetes](https://github.com/weaveworks/ignite)

In this example we will be running one node with the docker container runtime (soon to be depricated but this should work on any runtime) and the other one will be using the cos_containerd image which is required for gVisor nodes on GKE.


cos_containerd
We separate the decoy application and the honeypots onto different (VPSs) in this deployment. It is  safer to have them living on different machines. You can also deploy these within the same node if you want to (*not recommended or tested*).

# Deploying 2 Nodes on GKE (1 decoy, 1 honeypot)

### (optional pre-req) Install gcloud SDK (CLI)

https://cloud.google.com/sdk/docs/install

### 1.0 Create decoy Node using gcloud SDK (CLI)
```
gcloud container clusters create honey-cluster \
--disk-size 50 \
--num-nodes 1 \
--machine-type e2-small \
--no-enable-cloud-logging \
--no-enable-cloud-monitoring  \
```
### 2.0 Adding gVisor Node using gcloud (CLI)

Assuming you have an existing cluster like in step 1.0

Has to be:
- minimum ```machine-type=e2-standard-2``` 
- and ```--image-type=cos_containerd```
```
> gcloud container node-pools create honey-nodes \
  --cluster=honey-cluster \
  --machine-type=e2-standard-2 \
  --image-type=cos_containerd \
  --sandbox type=gvisor \
```
optional ```--node-version=node-version```.
```
Creating node pool honey-nodes...done.                                                                       
NAME         MACHINE_TYPE   DISK_SIZE_GB  NODE_VERSION
honey-nodes  e2-standard-2  100           1.18.17-gke.100
```


###  2.1 (alternative)  Create gVisor Node using Google Cloud Console (GUI) 

Has to be minimum ```e2-standard-2``` and ```cos_containerd```

![alttext](https://gvisor.dev/docs/tutorials/kubernetes/add-node-pool.png)

[gVisor Wordpress in Kubernetes Example](https://gvisor.dev/docs/tutorials/kubernetes/) 

### 3.0 connect your new gcloud cluster to your Kubernetes

```
> gcloud container clusters get-credentials honey-cluster
NAME           LOCATION        MASTER_VERSION   MASTER_IP       MACHINE_TYPE  NODE_VERSION     NUM_NODES  STATUS
honey-cluster  europe-west1-b  1.18.17-gke.100  11.222.333.444  e2-small      1.18.17-gke.100  1          RUNNING

> kubectl get nodes -o wide
NAME                                           STATUS   ROLES    AGE   VERSION            INTERNAL-IP   EXTERNAL-IP   OS-IMAGE                             KERNEL-VERSION   CONTAINER-RUNTIME
gke-honey-cluster-default-pool-...   Ready    <none>   33s   v1.18.17-gke.100   10.132.0.3    11.22.333.4   Container-Optimized OS from Google   5.4.89+          docker://19.3.14
```

### 4.0 Add the gVisor Runtime Class in deployment.yaml

- The decoy application (Crypto Price API)
- The Honeypots 
  - google-cloud create add this tag mage-type = cos_containerd
  - runtimeClassName:    # ADD THIS LINE # ADD THIS LINE

Please use honeypots and honey-clusters within authorized environments and networks  





Honey-clusters are Kubernetes clusters or deployments running multiple honeypots. These can be within a production environment. 


gcloud container clusters get-credentials honey-cluster