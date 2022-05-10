import select

# Local
import sys
sys.path.append("..")
import comms

# Constants
SERVER_PORT = 23456

# Globals
server_socket = None


def setup_server():
    global server_socket

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((comms.SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print("Server listening at %s:%d" %
          (comms.SERVER_HOST, SERVER_PORT))


def send_all_clients(msg):
    global clients

    for client in clients:
        client.sendall(msg)


