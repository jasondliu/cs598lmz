import select
import sys
import time

from . import logger
from . import utils

def _get_socket_path(name):
    return os.path.join(utils.get_socket_dir(), name)

def _get_socket_path_from_url(url):
    return _get_socket_path(url.split(':')[-1])

class SocketServer(object):
    def __init__(self, url):
        self.url = url
        self.socket_path = _get_socket_path_from_url(url)
        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.socket_path)
        self.socket.listen(1)
        self.connection = None

    def accept(self):
        self.connection, address = self.socket.accept()
        return self.connection

    def close(self):
       
