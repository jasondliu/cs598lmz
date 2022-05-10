import socket
import threading
import time
import queue
import random
import signal
import sys
import os

#global variables
port = 9999
max_connections = 5
buffer_size = 1024

#create socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

#bind socket to port and wait for connection from client
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(max_connections)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()

#Establish connection with client (socket must be listening)
def socket_accept():
    conn, address = s.accept
