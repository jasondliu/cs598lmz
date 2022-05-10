import socket
import struct
import time

from game_master.server_configurations import *

class Server:

    def __init__(self, game_class, game_name, game_config, port=DEFAULT_SERVER_PORT, verbose=False):
        """
        Initialize a new game server.
        :param game_class: The game class of the game to be played.
        :param game_name: The name of the game.
        :param game_config: The game configuration for this game.
        :param port: The port to run the server on.
        :param verbose: Whether to print verbose messages.
        """
        self.game = game_class(game_config)
        self.game_name = game_name
        self.game_config = game_config

        self.port = port
        self.verbose = verbose

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', self.port))
        self.socket.listen(2)
        self
