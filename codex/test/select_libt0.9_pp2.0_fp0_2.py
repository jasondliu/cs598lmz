import select
import socket as so
import sys as sys


LOG = logging.getLogger(__name__)
RESULT = "marda"

#Create connection
def create_connection(address, port):

    clientsocket = so.socket(so.AF_INET, so.SOCK_STREAM)
    clientsocket.connect((address, port))
    return clientsocket

class ConnectServer(object):

    CONNECTED = True
    SERVER_ADDRESS = "192.168.2.104"
    SERVER_PORT = PORT

    def __init__(self):
        self._clients = []
        self._server_socket = so.socket(so.AF_INET, so.SOCK_STREAM)
        #self._server.setsockopt(so.IPPROTO_TCP, so.TCP_NODELAY, 1)
        self._server_socket.bind((self.SERVER_ADDRESS, self.SERVER_PORT))
        self._server_socket.listen()
