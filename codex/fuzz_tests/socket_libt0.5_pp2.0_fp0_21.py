import socket
import json
from datetime import datetime
from time import sleep

from pydispatch import dispatcher
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication

from config import Config
from logger import Logger
from message_dispatcher import MessageDispatcher
from message_parser import MessageParser
from message_sender import MessageSender
from message_types import MessageTypes
from ui import Ui
from utils import Utils


class Client(QThread):

    # Signals
    signal_update_ui = pyqtSignal(list)
    signal_show_message = pyqtSignal(str)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(Config.SOCKET_TIMEOUT)
        self.message_parser = MessageParser()
       
