import selectors
import logging
import socket

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/home/jovyan/network-server.log',
                    filemode='w')


class NetworkServer:
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sel = selectors.DefaultSelector()
        self.messages = [b'Message 1 from client.', b'Message 2 from client.'] # this is to test server response
        
        self.create_socket()
        
    def create_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # to prevent "Address already in use" error
