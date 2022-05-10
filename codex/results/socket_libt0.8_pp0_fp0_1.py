import socket
import sys
import time
import thread
import random

def print_timestamp():
    print time.strftime("%H:%M:%S", time.localtime())

def print_error(e):
    print "Something bad happened!"
    print e

def send_packet(sock, packet):
    try:
        sock.send(packet)
    except socket.error, e:
        print_error(e)

def receive_packet(sock):
    try:
        return sock.recv(1024)
    except socket.error, e:
        print_error(e)
        return None

def print_ip(ip):
    print str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(ip[3])

class Command:
    def __init__(self):
        self.Id = 0
        self.Ip = [0, 0, 0, 0]
        self.Cmd = -1
        self.Len = 0
        self
