import socket
import threading
from _thread import *
import json
import os
import subprocess

names = []

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def threaded(client):
    while True:
       
        try:
            data = client.recv(4096)

            if not data:
                print('Disconnected')

                break
            
            elif data.decode() == 'check':
                client.send(str.encode(str(names)))
            elif data.decode() == 'search':
                try:
                    query = client.recv(4096)
                    search_query = query.decode()
                    print(search_query)

                    result = subprocess.check_output(['search.py', search_query])
                    print(result)
                    result  = result.decode()
                    client.send(str.
