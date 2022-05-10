import socket
import sys
import threading
import time

from . import data
from . import protocol

class Client:
    """
    A client for the Carriots API.
    """
    def __init__(self, api_key, client=None):
        """
        Create a new client.

        api_key -- the Carriots API key to use
        client -- the HTTP client to use (default: urllib3.PoolManager())
        """
        self.api_key = api_key
        self.client = client or urllib3.PoolManager()
        self.headers = {'User-Agent': 'carriots.py/' + __version__,
                        'Content-Type': 'application/json',
                        'Carriots.apikey': self.api_key}
        self.headers.update(protocol.get_headers())
        self.url = protocol.get_url()
        self.connections = {}
        self.connections_lock = threading.Lock()
        self.data_stream_id = None

    def create_connections(self, connections
