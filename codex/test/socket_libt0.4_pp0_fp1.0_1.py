import socket
import time
import threading
import sys
import os

# Global Variables

HOST = ''
PORT = 5000

# Creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to the host and port
s.bind((HOST, PORT))

# Listening for connections
s.listen(5)

print("Server started")

def clientthread(conn):
    while True:
        # Receiving from client
        data = conn.recv(1024)
        if not data:
            break
        print("Received from client: " + str(data))
        # Sending back to client
        conn.sendall(data)
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected with " + addr[0] + ":" + str(addr[1]))
    start_new_thread(clientthread, (conn,))

s.close()
