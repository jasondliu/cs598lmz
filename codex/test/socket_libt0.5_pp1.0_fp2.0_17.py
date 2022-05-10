import socket
import sys
import threading
import time

from _thread import *


def clientthread(conn):
    # Receive data from the client
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())
    # Close the connection
    conn.close()

def main():
    HOST = '127.0.0.1'
    PORT = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
    print('Socket bind complete')
    # Start listening on socket
    s.listen(10)
    print('Socket now listening')
    # Now keep talking with the client
    while True:
        conn, addr = s.accept()
