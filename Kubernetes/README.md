# Kubernetes Deployment for My Application

![kuberenetes](https://github.com/user-attachments/assets/0a763809-e01b-4854-821f-1498be63cc75)

This repository contains Kubernetes manifests to deploy and manage the application.

## Table of Contents

- [Kubernetes Deployment for My Application](#kubernetes-deployment-for-my-application)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Kubernetes Manifests](#kubernetes-manifests)
  - [Deployment](#deployment)
  - [Usage](#usage)
  - [ingress](#ingress)
  - [Cleanup](#cleanup)

## Prerequisites

- **minikube**

```bash
(minikube version: v1.35.0
commit: dd5d320e41b5451cdf3c01891bc4e13d189586ed)
```

- **kubectl**

```bash
Client Version: v1.32.2
Kustomize Version: v5.5.0
Server Version: v1.32.0
```

- **Docker** (for building images)

## Kubernetes Manifests

- **Namespace**: Defines a namespace for isolating resources.
- **LimitRange**: Sets resource limits for the namespace.
- **Deployment**: Manages the deployment of the application.
- **Service**: Exposes the application within the cluster.
- **Ingress**: Manages external access to the services.
- **Pod**: Defines the individual pods (if needed).
- **PVC**: Requests persistent storage.
- **ConfigMap**: Stores configuration data.
- **HPA**: Scales pods based on resource usage.

## Deployment

After Creating Secret.

```bash
kubectl apply -f namespace.yaml -f ingress.yaml -f pvc.yaml -f mysql_configmap.yaml -f mysql_service.yaml -f mysql_deployment.yaml -f django_service.yaml -f django_deployment.yaml -f HPA.yaml
```

## Usage

- **Check the status of all cluster**:

```bash
kubectl get all -n taskmanager-ns
```

then the application will be acess via the service

```bash
minikube service django -n taskmanager-ns
```

![Image](https://github.com/user-attachments/assets/2f8f5048-df3c-4fa4-bebb-3d37ef5147f2)

## ingress

u should put the ip of minikube in /etc/hosts file

```bash
minikube ip
echo < minikube ip > taskmanager.example.com > /etc/hosts
```

to open the service (app) `http://taskmanager.example.com`<TCP Port>`/`
![Image](https://github.com/user-attachments/assets/da3fa577-7f36-4740-83fd-575a67dc30c4)

## Cleanup

To delete all the resources created:

```bash
kubectl delete all --all -n taskmanager-ns
```
