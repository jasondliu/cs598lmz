import socket
import select
import sys
import json
import time
from thread import *

# Function to broadcast chat messages to all connected clients
def broadcast_data (sock, message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                CONNECTION_LIST.remove(socket)

def get_time():
    return time.strftime("%H:%M:%S", time.localtime())

def get_date():
    return time.strftime("%d/%m/%Y", time.localtime())

def get_date_time():
    return time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())

def get_time_stamp():
    return time.strftime("%d/%
