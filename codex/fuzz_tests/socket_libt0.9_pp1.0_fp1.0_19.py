import socket
import select
import sys

#CONSTANTS
HEADER_LENGTH = 10
HOST = "127.0.0.1"
PORT = 1234
running = True

#Network help functions

#get message length from header
def get_msg_len(header):
    msg_len = int(header.decode('utf-8').strip())
    return msg_len
         
#receive whole messages from client, return message
def receive_msg(client):
    try:
        header = client.recv(HEADER_LENGTH)

        if not len(header):
            return False
        
        msg_len = get_msg_len(header)
        msg = client.recv(msg_len)
        if not len(msg):
            return False
        return {"header": header, "data": msg}
    except:
        return False

#add header to actual msg (or message lenght)
def add_header_to_msg(msg):
    msg = bytes(f"{len(msg):<{HEADER_LENGTH}}",
