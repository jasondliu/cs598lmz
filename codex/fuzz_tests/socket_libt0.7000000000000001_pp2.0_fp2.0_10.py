import socket
import time

def main():
    # create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # reuse the same port
    # prevents the 'Address already in use' error
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind the socket to the local loopback address
    # and a port of our choice
    server_address = ('127.0.0.1', 10000)
    server.bind(server_address)

    # become a server socket
    server.listen(1)

    while True:
        # accept connections from outside
        print('waiting for a connection...')
        client_socket, client_address = server.accept()

        # start a new thread to handle incoming data
        client_thread = threading.Thread(
            target=handle_connection,
            args=(client_socket, client_address)
        )
        client_
