import select
import logging
import time
import threading
import Queue

class SocketServer(object):
    """
    A simple socket server.
    """

    def __init__(self, host, port, timeout=0.5, max_clients=10, max_data_size=4096):
        """
        Creates a server.

        :param host: The server host name.
        :param port: The server port.
        :param timeout: The timeout for the connection.
        :param max_clients: The maximum number of clients.
        :param max_data_size: The maximum data size.
        """
        self.host = host
        self.port = port
        self.timeout = timeout
        self.max_clients = max_clients
        self.max_data_size = max_data_size
        self.running = False
        self.listener = None
        self.clients = []
        self.client_data = {}
        self.client_buffers = {}
        self.client_lock = threading.Lock()
