import socket
import struct
from threading import Thread
from time import sleep
from datetime import datetime
from contextlib import contextmanager
import sys
from struct import *

from common import *

from config import Config
from cmd_parser import CmdParser

from engine import Engine
from logger import Logger
from game_logger import GameLogger
from game_state import GameState

from pygame_handler import PygameHandler
from camera_handler import CameraHandler
from image_handler import ImageHandler
from vision_handler import VisionHandler
from command_handler import CommandHandler
from game_handler import GameHandler

from ui import UI

from server import Server

from network import Network
from messages import *

from config import Config

from debug import Debug

class Application:
    def __init__(self):
        self.config = Config()
        self.debug = Debug(self)

        self.logger = Logger(self)
        self.logger.info("application", "starting")

        self.game_logger = GameLogger(self)
