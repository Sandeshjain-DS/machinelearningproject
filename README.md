## End to End MAchine Learning Project

1. Docker file checked in github

2. 

3. Github Workflow -docker action
4. Build CI and CD pipelines - in code
5. add keys of username and password in github secret
6. create same named repo in docker hub
7. Iam User In AWS
8. create ec 2 instance -ubuntu add inbound rules tcp  for streamlit 8501

## Docker Setup In EC2 commands to be Executed

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

docker login

## Configure EC2 as self-hosted runner:

DOCKER_USERNAME

DOCKER_PASSWORD

# nce code and yml is ready - star runner in ec2 ./run.sh

# to run in background   ./run.sh &

# to keep running runner after logout : nohup ./run.sh > runner.log 2>&1 &

 # delete all instance if not using
