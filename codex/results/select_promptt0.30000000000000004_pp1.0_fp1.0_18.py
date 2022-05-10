import select
# Test select.select()

import sys
import socket
import select

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

while True:
    # Wait for input from stdin & socket
    readable, writable, exceptional = select.select([sys.stdin, sock], [], [])
    for s in readable:
        if s is sock:
            data = s.recv(1024)
            if data:
                print('received "%s"' % data)
            else:
                print('closing', client_address)
                sock.close()
                sys.exit()
        else:
            # Read from keyboard
            message = sys.stdin.readline()
            sock.sendall(message)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
