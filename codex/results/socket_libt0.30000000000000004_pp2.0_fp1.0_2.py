import socket
import time
import threading
import sys

def send_message(sock, message):
    sock.sendall(message)

def recv_message(sock):
    data = sock.recv(1024)
    return data

def client_handler(sock):
    while True:
        data = recv_message(sock)
        print data

def main():
    server_address = ('localhost', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    print "Connected to server"
    t = threading.Thread(target=client_handler, args=(sock,))
    t.start()
    while True:
        message = raw_input("Enter message: ")
        send_message(sock, message)

if __name__ == '__main__':
    main()
