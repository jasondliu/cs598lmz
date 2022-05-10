import selectors
import socket
import types

# Create a TCP/IP socket
server_address = ('localhost', 10000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

# Create an event loop
selector = selectors.DefaultSelector()

# Register the server socket on the event loop
selector.register(fileobj=server, events=selectors.EVENT_READ, data=accept_connection)

def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    client_socket.setblocking(False)
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)

def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello world\n'.encode()
