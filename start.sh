#!/bin/bash

docker run maria1207/asvk-project
docker run --name serv -d -p 14990:14990 --entrypoint python maria1207/asvk-project server.py
docker run -a STDOUT -v /root:/app/data --name cli --entrypoint python maria1207/asvk-project cli.py
