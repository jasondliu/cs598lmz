import select
# Test select.select()
import socket
# Test socket.socket() and socket.connect()
import subprocess
# Test subprocess.Popen()
import sys
# Test sys.argv
import threading
# Test threading.Thread
import time
# Test time.sleep()
import unittest
import unittest.mock

# Test this module
from .. import client

# Test the server
from .. import server

def get_port():
    """
    Get a port number that is most likely not in use.
    """
    s = socket.socket()
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

class TestClient(unittest.TestCase):

    def setUp(self):
        self.port = get_port()
        self.server = server.Server(self.port)
        self.server.start()
        self.client = client.Client()

    def tearDown(self):
        self.server.stop()

    def test_connect_to_server(self):
