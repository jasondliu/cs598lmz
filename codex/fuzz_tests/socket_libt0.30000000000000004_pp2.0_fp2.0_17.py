import socket
import threading
import time
import sys
import os
import random

# Server IP
SERVER_IP = '127.0.0.1'
# Server Port
SERVER_PORT = 8888
# Client Port
CLIENT_PORT = 8889
# Client IP
CLIENT_IP = '127.0.0.1'
# Client Name
CLIENT_NAME = 'Client'
# Server Name
SERVER_NAME = 'Server'
# Client Socket
client_socket = None
# Server Socket
server_socket = None
# Client Address
client_address = None
# Server Address
server_address = None
# Client Thread
client_thread = None
# Server Thread
server_thread = None
# Client Thread Running
client_thread_running = False
# Server Thread Running
server_thread_running = False
# Client Thread Lock
client_thread_lock = threading.Lock()
# Server Thread Lock
server_thread_lock = threading.Lock()
# Client Thread Condition
client_thread_condition = threading.Condition()
# Server Thread Condition
server_thread_condition = thread
