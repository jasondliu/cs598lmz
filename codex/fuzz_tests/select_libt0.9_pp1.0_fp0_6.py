import select
import socket
import sys
import signal
import threading

# set up host and port
PORT = 53414
HOST = ""

# DNS servers list
servers = ["127.0.0.1", "127.0.0.2", "127.0.0.3"]

# create the new socket for server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind host and port to created socket
def bind_host_and_port(sock, host, port):
    try:
        sock.bind((host, port))
        print("listening on {}:{}".format(host, port))
    except socket.error as e:
        print(str(e))


# close_connection on recieved signal, stop accepting new connections and close connections with clients
def close_connection(signal, frame):
    print("\nServer has been closed")
    server_socket.close()
    sys.exit()


def process_client(clientsocket, addr):
    data = clientsocket.recv
