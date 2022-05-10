import socket
import platform
import sys
import threading
import time
import SocketServer
from optparse import OptionParser
import os
import logging

DEFAULT_PORT = 9999
DEFAULT_HOST = "localhost"

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)
        self.clients = []
        self.server_thread = None

    def get_client_by_ip(self, ip):
        for client in self.clients:
            if client.match_ip(ip):
                return client

