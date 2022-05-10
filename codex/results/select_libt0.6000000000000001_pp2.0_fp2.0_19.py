import select
import socket
import sys
import os
import struct
import threading
import signal
import time
import random
import Queue

class Server:
    def __init__(self, host, port):
        # List of all known clients
        self.clients = []

        # Dictionary of client names and their respective addresses
        self.clients_names = {}

        # List of all client addresses and the respective names
        self.clients_addresses = {}

        # Dictionary of client names and their respective sockets
        self.clients_sockets = {}

        # Dictionary of client names and their respective listening ports
        self.clients_listening_ports = {}

        # List of blocked client names
        self.blocked_clients = []

        # List of blocked client addresses
        self.blocked_clients_addresses = []

        # The server's listening port
        self.listening_port = port

        # The server's listening socket
        self.listening_socket = None

        # The server's listening thread
        self.listening_thread = None

        # The server's
