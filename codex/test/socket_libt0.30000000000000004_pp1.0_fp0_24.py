import socket
import sys
import os
import time
import threading
import subprocess
import re
import json
import random
import string

# Global variables
server_ip = '127.0.0.1'
server_port = 9999

# Function to send data to the server
def send_data(data):
    global server_ip, server_port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))
    sock.send(data)
    sock.close()

# Function to receive data from the server
def receive_data():
    global server_ip, server_port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))
    data = sock.recv(1024)
    sock.close()
    return data

# Function to send a command to the server
def send_command(command):
    global server_ip, server_port
