import socket
import sys
from threading import *
from SocketServer import *

from debug import *

from gi.repository import Gtk, Gdk,GObject
from pprint import pprint
from config import Config

from Queue import Queue, Empty
from threading import Thread
from time import sleep

from server import Server
from client import Client
from tictactoe import TicTacToe
from gomoku import Gomoku
from othello import Othello
from chess import Chess
from connectfour import ConnectFour

from gui import *

from stopwatch import StopWatch
from startscreen import StartScreen
from optionscreen import OptionScreen
from board_screen import BoardScreen
from endscreen import EndScreen
from waitingscreen import WaitingScreen

from client_event_handler import ClientEventHandler
from server_event_handler import ServerEventHandler

from message import *
from boards import *

from config import Config

# some globals we'll use

# path to our config file
config_file = "config.json"

# the config instance
config = Config(
