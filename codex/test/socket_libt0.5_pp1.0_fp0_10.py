import socket
import time
import threading
import os

def handle(client_socket):
    while True:
        request = client_socket.recv(1024)
        if not request:
            break
        print("[*] Received: %s" % request)
        client_socket.send("ACK!")
    client_socket.close()

def main():
    bind_ip = "0.0.0.0"
    bind_port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)

    print("[*] Listening on %s:%d" % (bind_ip, bind_port))

    while True:
        client, addr = server.accept()
        print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
        client_handler = threading.Thread(target=handle, args=(client,))
        client_handler.start()


