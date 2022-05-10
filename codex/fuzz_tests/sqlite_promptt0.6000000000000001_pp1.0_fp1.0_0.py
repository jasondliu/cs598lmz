import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")
import time
import datetime
import sys
import os

#def scan_ports(host, port):
#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    try:
#        con = s.connect((host,port))
#        print '%d:OPEN' % port
#        con.close()
#    except:
#        pass

def scan_ports(host, port,q):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((host,port))
        #print '%d:OPEN' % port
        #con.close()
        q.put(port)
        return True
    except:
        return False

def scan_ports_thread(host, port,q):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((host,port))
        #print '%d:
