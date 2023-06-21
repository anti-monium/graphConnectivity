#!/bin/bash

docker rm -f $(docker ps -qa)
docker volume prune
docker rmi maria1207/asvk-project
