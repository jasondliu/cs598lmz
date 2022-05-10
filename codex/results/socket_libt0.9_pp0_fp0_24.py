import socket
import time
import json
import datetime
import time
import threading
import Queue
import contextlib
import os

def GetFilePath():
    IsFile = False
    while not IsFile:
        try: 
            userfile = raw_input('\nPlease enter the location of gzipped log file (ex. /Users/pathtologfile.bin.gz): ')
            f = open(userfile, 'r')
            IsFile = True
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            IsFile = False
            
    if IsFile:
        print('received file: ' + userfile)
    return userfile

def GetIP():
    return raw_input('Please enter client IP: ')

def GetPort():
    return raw_input('Please enter port(ex. 5000): ')

def GetHost():
    return raw_input('Please enter host IP: ')

def GetQuery():
    return raw_input('Please enter
