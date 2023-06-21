#!/usr/bin/python3.8

import socket

f = open("data/input.txt")
connection = socket.socket()
connection.connect(("172.17.0.1", 14990))
l = f.readline()

while l != "":
    l = l.encode("ascii")
    connection.send(l)
    l = f.readline()
while True:
    data = connection.recv(1024)
    ans = data.decode("ascii")
    if ans != '':
        print(data.decode("ascii"))
    if not data:
        break
f.close()
connection.close()
