import socket
import threading
import time
import os
import sys
import subprocess
import shlex
import platform

# Global variables

# For the server
host = ''
port = 9999

# For the client
connected = False

# For the chat
user_name = ''
user_name_len = 0
chat_name = ''
chat_name_len = 0

# For the server
clients = []
client_names = []
client_names_len = []
client_sockets = []
client_ips = []
client_ports = []

# For the client
client_name = ''
client_name_len = 0

# For the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(10)

# For the client
