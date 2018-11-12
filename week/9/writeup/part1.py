#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

hash_fp = open("../hashes",'r')

hashes = hash_fp.readlines()
stripped_hashes = []
for x in hashes:
    stripped_hashes.append(x.strip())

password = wordlist.readlines()
strip_pass = []
for x in password:
    strip_pass.append(x.strip())


for salt in salts:
    for x in strip_pass:
        salt_password = salt+x
        h = hashlib.sha512(salt_password)
        for y in stripped_hashes:
            if(y == h.hexdigest()):
                print("Salt: " + salt + "\n" + "Password: " + x)
