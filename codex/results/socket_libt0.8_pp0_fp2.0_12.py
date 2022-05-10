import socket
import sys
import select
import thread
global client_list
global variable_list
global variable_list_server
#global variable_list_client
global variable_value

full = []
variable_list = {}
variable_list_server = {}
variable_value = {}
client_list = []
server_list = []
#variable_list_client = []

def broadcast(sock, message):
    for socket in full:
        if socket != server_socket and socket != sock:
            try:
                socket.send(message)
            except:
                socket.close()
                full.remove(socket)

def broadcast2(sock, message):
    for socket in server_list:
        if socket != server_socket2 and socket != sock:
            try:
                socket.send(message)
            except:
                socket.close()
                server_list.remove(socket)

def broadcast3(sock, message):
    for socket in client_list:
        if socket != server_socket3 and socket != sock:
            try:
                socket.send(
