import socket
import sys
from threading import Thread

from coders import coder
from game import Game
from pprint import pprint
from player import Player


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


def handle_connection(connection, player_id, game):
    """Handle an incoming connection."""
    print('A new connection has been established!')
    while True:
        try:
            data = connection.recv(32)
            if data:
                game.process_message(player_id, data)
        except:
            print('Lost connection!')
            break
    connection.close()


def main():
    # declare a game
    game = Game()

    # get ip address to listen on
    host
