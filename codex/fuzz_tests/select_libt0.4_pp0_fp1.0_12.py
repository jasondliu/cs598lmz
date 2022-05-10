import select
import socket
import sys
import threading
import time

# -----------------------------------------------------------------------------
#
# Server class
#
# -----------------------------------------------------------------------------

class Server:

    # -------------------------------------------------------------------------
    #
    # __init__
    #
    # -------------------------------------------------------------------------

    def __init__(self, host, port, backlog=5):
        self.__host = host
        self.__port = port
        self.__backlog = backlog
        self.__server = None
        self.__clients = {}
        self.__addresses = {}
        self.__running = False
        self.__thread = None

    # -------------------------------------------------------------------------
    #
    # start
    #
    # -------------------------------------------------------------------------

    def start(self):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server.bind((self.__host, self.__port))
        self.__server.listen(self
