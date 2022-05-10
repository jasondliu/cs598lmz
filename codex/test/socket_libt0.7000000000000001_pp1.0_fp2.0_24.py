import socket
import time

PORT = 1234

def recieve_message(sock):
    data = ""
    try:
        data = sock.recv(1024)
        if data:
            return data
    except:
        pass
    return False

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', PORT))
    server_socket.listen(1)
