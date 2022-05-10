import selectors
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

from lib.logger import log
from lib.config import Config
from .connection import Connection
from .protocol import Protocol
from .player import Player
from .game import Game
from .games import GameManager


class Server(object):

    def __init__(self, config: Config) -> None:
        self.config = config

        self.protocol = Protocol()
        self.manager = GameManager()
        self.players = set()
        self.connections = set()
        self.queue = Queue()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.config.host, self.config.port))
        self.socket.listen()
        self.socket.setblocking(False)

        self.selector = selectors.DefaultSelector()
        self.select
