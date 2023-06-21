#!/usr/bin/python3.8

import socket
from random import randint
from os import remove

while True:
    net_struct = list()     #net_struct содержит рёбра графа, задающего сеть
    users = {}              #словарь: ключ - имя вышки, значение - число пользователей
    towers = list()         #вышки мобильной связи - вершины графа
    control_towers = set()  #множество вышек для проверки корректности ввода
    n = 1                   #для подсчёта строк
    fl = 0                  #флаг для вывода всех ошибок в строках

    num = randint(0, 21122142342)
    name = str(num) + ".txt"
    
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", 14990))
    sock.listen(1)
    connection, addr = sock.accept()
    
    f = open(name, 'w')
    data = connection.recv(65536)
    l = data.decode("ascii")
    f.writelines(l)
    f.close()
    f = open(name, 'r')
    
    l = f.readline()
    while l != "\n" and l != '':
        l = l.split()
        if len(l) != 2:
            msg = "IN INPUT FILE - LINE" + str(n) + "\n\tInput error: incorrect string length"
            connection.send(msg.encode("ascii"))
            fl = 1
        l.sort()
        net_struct.append(l)
        try:
            control_towers.add(l[0])
            control_towers.add(l[1])
        except:
            fl = 1
        l = f.readline()
        n = n + 1
    net_struct.sort()
    l = f.readline()
    n = n + 1
    minimal = 0
    while l != "":
        tmp = l.split()
        if len(tmp) != 2:
            msg = "IN INPUT FILE - LINE" + str(n) + "\n\tInput error: incorrect string length"
            connection.send(msg.encode("ascii"))
            fl = 1
        try:
            users[tmp[0]] = int(tmp[1])
            minimal += int(tmp[1])
            towers.append(tmp[0])
        except ValueError:
            msg = "IN INPUT FILE - LINE" + str(n) + "\n\tInput error: int expected"
            connection.send(msg.encode("ascii"))
            fl = 1
        except IndexError:
            fl = 1
        l = f.readline()
        n = n + 1
    towers.sort()           
    minimal = minimal ** 2
    f.close()
    remove(name)
    
    if fl == 1:
        connection.close()
        quit()
    if len(towers) > len(set(towers)):
        msg = "IN INPUT FILE\n\tInput error: user's number declared for one tower more than once"
        connection.send(msg.encode("ascii"))
        connection.close()
        quit()
    if len(control_towers) > len(towers):
        msg = "IN INPUT FILE\n\tInput error: user's number declared not for all towers"
        connection.send(msg.encode("ascii"))
        connection.close()
        quit()
    if not (set(towers) >= control_towers):
        msg = "IN INPUT FILE\n\tInput error: the declared sets of towers are incorrect"
        connection.send(msg.encode("ascii"))
        connection.close()
        quit()
        
    towers_connectivity = {}        
    for tower in towers:
        towers_copy = list(towers)
        towers_copy.remove(tower)
        towers_connectivity[tower] = users[tower]
        while towers_copy != list():
            new_net = list()
            new_net.append(towers_copy[0])
            towers_copy.remove(towers_copy[0])
            for l in net_struct:
                if l[0] == tower or l[1] == tower:
                    continue
                if l[0] in new_net and l[1] not in new_net:
                    new_net.append(l[1])
                    if l[1] in towers_copy:
                        towers_copy.remove(l[1])
                elif l[1] in new_net and l[0] not in new_net:
                    new_net.append(l[0])
                    if l[0] in towers_copy:
                        towers_copy.remove(l[0])
            s = 0
            for tw in new_net:
                s = s + users[tw]
            towers_connectivity[tower] = towers_connectivity[tower] + s ** 2
        minimal = min(minimal, towers_connectivity[tower])
        
    prime_towers = list()
    for tw in towers_connectivity:
        if minimal == towers_connectivity[tw]:
            prime_towers.append(tw)
    if len(prime_towers) > 0:
        msg = str(prime_towers)
        connection.send(msg.encode("ascii"))
    else:
        msg = "Empty file"
        connection.send(msg.encode("ascii")) 
    connection.close()
print("hui")
    
    
    

















