import socket
import time
import threading
import sys

def read_data(conn):
    while 1:
        data = conn.recv(1024)
        if not data:
            print("Connection has been closed")
            return
        else:
            print("Data recived from %s:%s" % (addr[0],addr[1]))
            print("Data: %s" %data)
            conn.send("data recived")
        
    
#host IP
host = '192.168.0.27'
port = 8743

#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#bind socket
s.bind((host, port))

print("Listening on PORT: %d" % port)

#listen for incoming connections
s.listen(1)

while 1:
    conn, addr = s.accept()
