import select
import time
import signal
import sys

class ProxyServer:

    def __init__(self, port=8080, host='127.0.0.1', max_conn=5):
        signal.signal(signal.SIGINT, self.shutdown)
        self.port = port
        self.host = host
        self.max_conn = max_conn
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(self.max_conn)
        self.inputs = [self.server_socket]
        self.outputs = []
        self.message_queues = {}

    def shutdown(self, signum, frame):
        print('\n[*] Shutting down...')
        self.server_socket.close()
