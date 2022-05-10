import select
import socket
import errno
import re

from .log import Logger
from .http import HttpProcessor

class HttpServer:
    def __init__(self, config):
        self.config = config
        self.log = Logger(config)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        try:
            self.server_socket.bind((self.config.server_name, self.config.server_port))
            self.server_socket.listen(128)
            self.server_socket.setblocking(0)
        except Exception as ex:
            self.log.error('{} exiting with exception'.format(self.__class__.__name__), ex)
            raise ex
        self.log.info('{} started'.format(self.__class__.__name__))
        self.log.info
