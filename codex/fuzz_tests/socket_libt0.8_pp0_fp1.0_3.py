import socket
import sys

def chat(sock):
    while 1:
        data = raw_input("")
        if data != "":
            sock.sendall(data)
        else:
            break
        data = sock.recv(4096)
        print data

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'conne
