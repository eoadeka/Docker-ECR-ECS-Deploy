# ECS-Docker-Deploy

This project involves deploying a Docker image of a "quote application" to ECR and launching a task into an ECS cluster to expose the app to the internet. The aim is to ensure a seamless and scalable deployment process for a containerised application.

The execution was carried out in the CLI as a challenge.

## Architecture Design
![DockerAppDeployECS](https://github.com/ella-adeka/Docker-ECR-ECS-Deploy/assets/70539937/454ff89d-dfdb-4171-9660-079ecf53a819)

## Steps
- Build a local Docker image
- Upload it to ECR
- Create an ECS Cluster
- Configure a task to run local image
- Launch a task into the cluster and expose the app to the internet via VPC

## Results
App running on localhost
![quote_localhost](https://github.com/ella-adeka/Docker-ECR-ECS-Deploy/assets/70539937/cbfcb633-7429-4800-915e-f877dfa6c8bf)

Successful `docker push` to ECR
![push_successful](https://github.com/ella-adeka/Docker-ECR-ECS-Deploy/assets/70539937/9f48d0ed-2a5d-4347-bbd5-dd756627251b)

Image in ECR
![image_in_ecr](https://github.com/ella-adeka/Docker-ECR-ECS-Deploy/assets/70539937/e2adb0a8-aa25-49d8-aa27-07989408f217)

ECS Cluster
![CLUSTER](https://github.com/ella-adeka/Docker-ECR-ECS-Deploy/assets/70539937/f387c113-c32d-408c-87ed-673ce822420a)

Task running successfully on ECS Cluster
![TASK_RUNNING](https://github.com/ella-adeka/Docker-ECR-ECS-Deploy/assets/70539937/9dd923f8-4341-4671-937c-a8112b7ab816)
