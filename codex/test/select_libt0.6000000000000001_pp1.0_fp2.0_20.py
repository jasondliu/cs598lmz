import select
import socket
import sys
import traceback
from threading import Thread

# Connecting to the server
def create_socket(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print('Failed to create socket. Error code: ' + str(msg[0]) + ', Error message: ' + msg[1])
        sys.exit()

    print('Socket created')

    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        # Could not resolve
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    # Connect to remote server
    s.connect((remote_ip, port))

    print('Socket connected to ' + host + ' on ip ' + remote_ip)
    return s

# Receiving data from the server
def receive_data(s):
    while True:
        socket_list = [sys.stdin, s]

        # Get the list of
