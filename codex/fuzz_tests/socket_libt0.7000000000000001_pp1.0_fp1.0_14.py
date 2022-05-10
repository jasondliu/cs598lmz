import socket
import sys
import time
from random import randint

from networking.network_server import NetworkServer


class GameServer(NetworkServer):
    def __init__(self, port=None, game_type=None):
        super().__init__(port)
        self.game_type = game_type
        self.players = []

    def get_game_type(self):
        return self.game_type

    def do_initial_handshake(self, connection):
        player_id = len(self.players)
        connection.sendall(str(player_id).encode())

    def add_player(self, player):
        self.players.append(player)

    def get_players(self):
        return self.players

    def get_players_count(self):
        return len(self.players)

    def start(self):
        # Bind the socket to the port
        try:
            self.server_socket.bind((self.host, self.port))
        except socket.error as msg:
            print('Bind failed. Error Code : {} Message
