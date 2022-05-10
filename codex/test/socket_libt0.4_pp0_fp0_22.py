import socket
import sys
import os
import time
from threading import Thread
import select
from threading import Lock

# lock = Lock()

def get_file_size(file_name):
    file_size = os.path.getsize(file_name)
    return file_size

def receive_file(sock, file_name, file_size):
    print("Receiving file: " + file_name + " of size: " + str(file_size) + " bytes")
    file_data = sock.recv(file_size)
    print("Received file: " + file_name + " of size: " + str(file_size) + " bytes")
    return file_data

def receive_file_size(sock):
    file_size = sock.recv(1024)
    return file_size

def receive_file_name(sock):
    file_name = sock.recv(1024)
    return file_name

