import select
import socket
import sys
import time
import threading

def open_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('localhost', 5555))
        sock.listen(5)
    except socket.error as e:
        print("Socket error: %s" % e)
        sys.exit(1)
    return sock

def run_server(sock):
    while True:
        try:
            connection, client_address = sock.accept()
        except IOError as e:
            if e.errno == errno.EINTR:
                continue
            else:
                raise
        try:
            handle_request(connection, client_address)
        finally:
            connection.close()

def handle_request(connection, client_address):
    while True:
        data = connection.recv(1024)
        if 'close'
