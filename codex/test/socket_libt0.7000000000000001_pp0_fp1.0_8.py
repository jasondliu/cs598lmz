import socket
from urllib.parse import urlparse
from socketserver import StreamRequestHandler, TCPServer
import requests
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()

class ProxyHandler(StreamRequestHandler):

    def handle(self):
        print('{} connected'.format(self.client_address[0]))
        # get the client request
        request = self.rfile.readline().decode().split()
        print(request)
        # if the request is not empty
        if request:
            # parse the url and get the host and port
            url = urlparse(request[1])
            host, port = url.netloc, url.port or 80
            # create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # connect to the host
            sock.connect((host, port))
            # send the rest of the request through the socket
            sock.send(self.rfile.read())
            # set the socket to non-blocking mode
            sock
