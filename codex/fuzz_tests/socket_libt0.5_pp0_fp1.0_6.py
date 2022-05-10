import socket
import time

def send_data(sock, data):
    """Send data to the server.
    """
    if not isinstance(data, bytes):
        data = data.encode()
    sock.sendall(data)

def receive_data(sock, size=1024):
    """Receive data from the server.
    """
    data = sock.recv(size)
    return data.decode()

def get_command(sock):
    """Get the command from the server.
    """
    data = receive_data(sock)
    return data

def send_response(sock, response):
    """Send the response to the server.
    """
    send_data(sock, response)

def get_file_data(sock):
    """Get the file data from the server.
    """
    data = receive_data(sock)
    return data

def send_file_data(sock, file_data):
    """Send the file data to the server.
    """
    send_data(sock
