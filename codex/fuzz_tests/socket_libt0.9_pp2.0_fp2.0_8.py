import socket
import sys
import os
import getpass
import hashlib
from Crypto.Hash import SHA256
from Crypto.Hash import HMAC
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5



#trying to input a symmetric key
print "This is Bob"
os.system('tty > keytemp.txt')
tty = open('keytemp.txt', 'r')
mykey = tty.read()
os.system('stty -echo; head -n 1 keytemp.txt | md5sum > md5temp.txt')
os.system('head -c 32 keytemp.txt | sha256sum > sha256temp.txt')
#os.system('stty echo; head -c 16 keytemp.txt | sha1sum > sha1temp.txt')
print "Please type in your password: "
pwd1 = getpass.getpass()
print "Please retype in your password: "
pwd2 = getpass.getpass()
if pwd1 != pwd2:
    print
