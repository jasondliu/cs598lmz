import select
import socket
import time
import threading
import traceback
import Queue

import pygame

import Utils

logger = Utils.getLogger("Server")

class Server(object):
    """
    The server.
    """

    # The port to listen on.
    PORT = 50000

    def __init__(self, game):
        """
        Initialize the server.
        """

        # A reference to the game.
        self.game = game

        # The server socket.
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(("", self.PORT))
        self.server.listen(5)

        # A list of client sockets.
        self.clients = []

        # A list of client threads.
        self.clientThreads = []

        # A list of client IDs.
        self.clientIDs = []
