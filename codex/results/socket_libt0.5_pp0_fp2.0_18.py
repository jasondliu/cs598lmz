import socket
import sys
import time
import threading
import datetime

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def handle_client(client):
    try:
        # Receive the data in small chunks and retransmit it
        while True:
            data = client.recv(1024)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                client.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    except:
        pass
    finally:
        client.close()

def handle_thread(client):
    while True:
        client.sendall(str(datetime.dat
