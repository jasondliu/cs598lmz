import select
import socket
import sys

class Server(object):

    def __init__(self):
        self.host = 'localhost'
        self.port = 9999
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []

