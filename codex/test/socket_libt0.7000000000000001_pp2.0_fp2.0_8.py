import socket
import subprocess
import time
import sys

from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.iostream import StreamClosedError
from tornado import gen
from tornado.tcpclient import TCPClient
from tornado.options import define, options, parse_command_line

define("host", default='127.0.0.1', help="TCP server host")
define("port", default=8888, help="TCP port to connect to")
define("send_interval", default=3, help="Interval in seconds between send")

PORT = 8888
SERVER_IP = "127.0.0.1"
# HOST = socket.gethostname()

# SERVER_IP = socket.gethostbyname(socket.gethostname())

class EchoClient(object):
    """A simple echo client that sends messages at a regular interval."""
    def __init__(self, url, send_interval):
        self.url = url
        self.send_interval = send_interval
        self._running = False

