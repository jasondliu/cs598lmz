import select
import socket
import sys
import threading

class Server(object):
    def __init__(self, port, handler):
        self.port = port
        self.handler = handler
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', self.port))
        self.sock.listen(1)

        inputs = [self.sock]
        outputs = []
        message_queues = {}

        while inputs:
            readable, writable, exceptional = select.select(inputs, outputs, inputs)

            for s in readable:
                if s is self.sock:
                    connection, client_address = s.accept()
                    connection.setblocking(0
