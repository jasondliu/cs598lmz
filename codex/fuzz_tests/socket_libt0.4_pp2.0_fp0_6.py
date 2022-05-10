import socket
import threading
import time

from .. import utils


class Server(object):
    def __init__(self, port=8000, host=None, backlog=5, reuse_addr=True,
                 reuse_port=True, timeout=10, max_connections=100,
                 max_connections_per_ip=0, max_requests_per_connection=0,
                 max_requests_per_ip=0, request_queue_size=5,
                 request_timeout=60, shutdown_timeout=60,
                 socket_options=None, ssl_context=None):
        self.port = port
        self.host = host
        self.backlog = backlog
        self.reuse_addr = reuse_addr
        self.reuse_port = reuse_port
        self.timeout = timeout
        self.max_connections = max_connections
        self.max_connections_per_ip = max_connections_per_ip
        self.max_requests_per_connection = max_requests_per_connection
        self.max_
