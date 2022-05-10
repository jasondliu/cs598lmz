import socket
import sys
import time
import threading
import os
import struct
import hashlib
import pickle

BUFFER_SIZE = 1024

def get_file_md5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

def get_file_size(filename):
    size = os.path.getsize(filename)
    return size

def get_file_name(filename):
    temp = filename.split('/')
    return temp[len(temp)-1]

def get_file_path(filename):
    temp = filename.split('/')
    path = ''
    for i in range(0,len(temp)-1):
        path = path + temp[i] + '/'
    return path

def get_file
