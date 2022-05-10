import socket
import sys, os, time
from Crypto.Cipher import AES

header = sys.argv[1]

if len(sys.argv) > 1:
    HEADER = sys.argv[1]
else:
    HEADER = 10
# Create a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10001)
sock.connect(server_address)

