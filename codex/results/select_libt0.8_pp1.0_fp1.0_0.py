import select
import socket
import sys
import threading

from utils import *

#TODO: multithread
#TODO: send all connections to other server on exit
#TODO: check if connection exists

args = get_args()
connections = {}

def handle_client(client, address):
    sid = hex(id(client))

    while True:
        try:
            # get data from client
            data = client.recv(1024)
            if data:
                # forward data to server
                connections[sid].send(data)
            else:
                # connection closed
                client.close()
                # raise exception to terminate loop
                raise Exception('')
        except Exception as e:
            # close client connection
            client.close()
            # close server connection
            connections[sid].close()
            break

def handle_server(server, address):
    # accept connection from server
    conn = server.accept()
    sid = hex(id(conn[0]))
    connections[sid] = conn[0]

    while True:
