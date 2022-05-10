import socket
import time
import threading
import sys

server_ip = '127.0.0.1'
server_port = 5000

def client_thread(client_socket):
    global server_ip
    global server_port
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        print(message.decode())
        message = input("-> ")
        client_socket.send(message.encode())
    client_socket.close()

def main():
    global server_ip
    global server_port
    client_socket = socket.socket()
    client_socket.connect((server_ip,server_port))
    threading.Thread(target=client_thread, args=(client_socket,)).start()
    while True:
        message = input("-> ")
        client_socket.send(message.encode())
    client_socket.close()

if __name__ == "__main__":
    main()
