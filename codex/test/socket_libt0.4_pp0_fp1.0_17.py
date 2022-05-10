import socket
import sys
import time

from . import common
from . import settings

def main():
    """
    The main function for the client.
    """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (settings.SERVER_IP, settings.SERVER_PORT)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

