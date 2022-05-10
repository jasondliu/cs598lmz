import socket
import sys

host = 'localhost'

def echo_server(port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print("Starting up echo server on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(1)
 
    while True:
        print("Waiting for connections")
        client_sock, client_addr = sock.accept()
        print("Client connected:", client_addr)
        handle_client(client_sock)
        client_sock.close()
        print("Connections closed")

def handle_client(client_sock):
    while True:
        data
