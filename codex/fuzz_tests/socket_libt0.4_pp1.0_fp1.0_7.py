import socket
import threading
import time
import random
import datetime

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print('[*] Received: %s' % request)
    client_socket.send(b'ACK!')
    client_socket.close()

def tcp_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print('[*] Listening on %s:%d' % (ip, port))
    while True:
        client, addr = server.accept()
        print('[*] Accepted connection from: %s:%d' % (addr[0], addr[1]))
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def udp_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_
