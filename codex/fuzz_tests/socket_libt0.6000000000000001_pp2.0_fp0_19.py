import socket
import time
from subprocess import check_output
from threading import Thread

from mpi4py import MPI

from .util import Hosts, log


# TODO: should this be configurable?
port = 8888


class Client:
    def __init__(self, host, env):
        self.host = host
        self.env = env
        self.socket = None

    def connect(self):
        # TODO: this will hang until the server is up
        self.socket = socket.create_connection((self.host, port))

    def send(self, msg):
        self.socket.sendall(msg + "\n")

    def recv(self):
        # TODO: this will hang until the server responds
        return self.socket.recv(1024)

    def close(self):
        # TODO: this will hang until the server is up
        self.socket.close()


class ClientThread(Thread):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.
