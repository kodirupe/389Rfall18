#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import time
host = "142.93.117.193"   # IP address or URL
port =  7331  # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)
print(data)
#3  5  
arr = data.split()
hash = getattr(hashlib,arr[12])(arr[15])
hex = hash.hexdigest()
s.send(hex+'\n')
while("You win!" not in data):
    data = s.recv(1024)
    if("You win!" not in data):
        print(data)
        arr = data.split()
        hash = getattr(hashlib,arr[4])(arr[7])
        hex = hash.hexdigest()
        s.send(hex+'\n')
print(data)
# close the connection
s.close()
