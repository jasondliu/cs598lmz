import socket
import time
from os import sys

from evolution.core import ModelBase
from evolution.core.database_base import DatabaseBase
from evolution.core.client_base import ClientBase
from evolution.core.receiver import Receiver
from evolution.core.server_base import ServerBase

from evolution.snake import SnakeServer, SnakeClient

from evolution.server_config import DatabaseServerConfig, ClientServerConfig
from evolution.snake.snake_config import SnakeConfig
from evolution.snake.snake_database import SnakeDatabase

from evolution.server.server import EvolutionServer

from evolution.snake.game import Game
from evolution.snake.snake import Snake
from evolution.snake.field import Field
from evolution.snake.food import Food
from evolution.snake.ai import SnakeAI


from evolution.core.manager import Manager


class SnakeManager(Manager):
    def __init__(self):
        config = SnakeConfig()

        self.config = config

        rec = Receiver()

        self.receiver = rec

        rec.add_receiver(self)

        self.c
