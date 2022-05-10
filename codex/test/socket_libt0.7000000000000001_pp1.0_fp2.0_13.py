import socket
import threading

server_address = ("192.168.1.113", 5555)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind((server_address))

def send(connectionSocket):
    while True:
        message = raw_input("")
        client_socket.sendto(message.encode(), server_address)

def receive(connectionSocket):
    while True:
        message, addr = client_socket.recvfrom(1024)
