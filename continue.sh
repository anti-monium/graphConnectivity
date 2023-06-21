#!/bin/bash

docker rm cli
docker run -a STDOUT -v /root:/app/data --name cli --entrypoint python maria1207/asvk-project cli.py
