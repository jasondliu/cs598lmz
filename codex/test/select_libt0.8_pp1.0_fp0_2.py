import selectors
import struct
import time
import types
import queue
import json
import os

from SocketClient import socket_client

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


class Config:
    def __init__(self, path):
        self.config = configparser.ConfigParser()
        self.config.read(path)

    def __getattr__(self, key):
        try:
            return self.config.get('DEFAULT', key)
        except configparser.NoOptionError:
            raise AttributeError(key)


class Server(object):
    def __init__(self, config_path):
        self.config = Config(config_path)

        self.host = self.config.host
        self.port = int(self.config.port)
        self.address = (self.host, self.port)

        self.selector = selectors.DefaultSelector()
        self.listener = None

        self.data = queue.Queue()

        self.__init_socket()

        self.socket
