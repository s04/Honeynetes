# Honey-clusters (/ˈklʌstə ˈhʌni/)

This is the repository for a 

## **Sandboxing untrusted honeybot workload in Kubernetes**

These are the yaml files, scripts and code for my Final Year Project / Bachelors dissertation at Trinity College Dublin and will no longer be maintained beyond: May 2021.

Honeypots are intentionally exposed networks, systems or applications. One can study the attacks made on honeypots in order to get real time data about what exploits are being used.

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

In this example we will be running one node with the docker container runtime (soon to be deprecated but this should work on any runtime) and the other one will be using the cos_containerd image which is required for gVisor nodes on GKE.

Please use honeypots and honey-clusters within authorized environments and networks. I am not responsible for any consequences or billing due to this code.

