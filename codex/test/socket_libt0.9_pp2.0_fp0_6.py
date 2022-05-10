import socket
import sys
import thread

## This is TCP receiver.

SERVER_IP = '127.0.0.1'
SERVER_PORT = 1300
BYTES = 1024
RUNNING = True


# Create receiver
receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


