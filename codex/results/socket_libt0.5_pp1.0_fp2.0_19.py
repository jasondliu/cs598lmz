import socket
import time
import threading

SERVER_IP = "127.0.0.1"
SERVER_PORT = 7000
BUFFER_SIZE = 1024

# Initialize the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
client_socket.sendall(b'hello')

# Receive the message from the server
data = client_socket.recv(BUFFER_SIZE)
print("Received: ", data.decode())

# Close the socket
client_socket.close()
