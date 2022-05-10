import socket
from time import time
from random import randint

HOST = input('Escolha o ip: ')
PORT = int(input('Escolha a porta: '))
NUM_PLAYERS = int(input('Escolha o numero de jogadores(2 ou 3): '))

class Game(object):

    def __init__(self, HOST, PORT, NUM_PLAYERS):
        self.players = []
        self.running = True

        self.HOST = HOST
        self.PORT = PORT
        self.NUM_PLAYERS = NUM_PLAYERS
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind((self.HOST, self.PORT))
