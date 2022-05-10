import socket
import select
import sys


def _process_client_message(message, server_socket):
    print('Message received: {0}'.format(message))

    if message == 'quit':
        server_socket.close()
        sys.exit()
    else:
        resp = message.upper()
        return resp


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(10)
    open_client_sockets = []
    messages_to_send = []

    while True:
        # Check readable and writable sockets
        readable, writable, error = select.select(
            open_client_sockets, [], [])

        # Process readable sockets
        for client in readable:
            message = client.recv(1024)
            if message:
                resp = _process_client
