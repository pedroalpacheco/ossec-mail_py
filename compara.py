#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import os
from sendmails import gomail

#PedroAlPacheco - 24/07/2017
#No more customizations were placed because the script runs on server in production

arqlerbinario = '/var/ossec/logs/alerts/alerts.log'
arqstoragehash = '/var/ossec/logs/alerts/hashlog.txt'

def crialog():
    existe = os.path.isfile(arqstoragehash)
    if existe == False:
        open(arqstoragehash, "wb")
        print("Log criado!")
    else:
        print("Log já existe!")

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

crialog()

hashnew = hash_file(arqlerbinario)

arqold = open(arqstoragehash, 'r')
hashold = arqold.read()



# storage hash new
arq = open(arqstoragehash, 'w')
arq.write(hashnew)
arq.close()

# DEBUG
#print("New hash: "+hashnew)
#print("Old hash: "+hashold)


if hashnew == hashold:
    print ("Hash IGUAIS!")
else:
    print('Enviando e-mail...')
    gomail()

