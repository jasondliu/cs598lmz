import socket
import urllib.parse
import signal
from core.util import *


class Server:
    def __init__(self, address, port, doc_root: str, max_connections=5):
        # Check if doc_root is a valid path
        if not os.path.isdir(doc_root):
            raise ValueError('Server root folder is not a valid path.')

        self.max_connections = max_connections
        self.doc_root = doc_root

        # Create the socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout for 2 seconds so socket doesn't block forever
        self.server_socket.settimeout(2)

        # Rebind socket if it is already in use
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Try to bind the socket
        try:
            self.server_socket.bind((address, port))
        except Exception as e:
            raise
