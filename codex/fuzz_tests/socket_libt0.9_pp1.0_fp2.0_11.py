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

try:
    if os.path.isfile(HEADER):
        with open(HEADER, 'rb') as f:
            msg = f.read(1024)
            while msg:
                sock.send(msg)
                msg = f.read(1024)
    else:
        sock.send(HEADER)

    offset = 0
    uploadFile = open('fromServer', 'wb')
    filenameSize = struct.unpack('Q', sock.recv(struct.calcsize('Q')))[0]
    filename = sock.recv(filenameSize)
    key = os.
