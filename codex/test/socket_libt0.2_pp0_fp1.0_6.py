import socket
import sys
import time
import threading
import os
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def get_data(sock):
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
