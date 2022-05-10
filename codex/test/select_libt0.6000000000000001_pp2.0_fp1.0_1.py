import selectors
import socket
import sys
import threading
import time
import traceback
import os

# A thread that handles one client.
class Client:

    def __init__(self, sock, address):
        # The socket for this client.
        self.sock = sock
        # The address of this client.
        self.address = address
        self.sock.setblocking(False)
        # The input buffer for this client.
        self.ibuffer = bytearray()
        # The output buffer for this client.
        self.obuffer = bytearray()
        # The selector for this client.
        self.sel = selectors.DefaultSelector()
        # This client's current state.
        self.state = None
        # This client's current game.
        self.game = None
        # This client's current player.
        self.player = None
        # This client's current game state.
        self.gamestate = None
        # This client's current game action.
        self.action = None
        # This client's current game target.
        self
