import socket
import sys
import threading
import random
import time

from . import data_structures
from . import net
from . import utils
from . import config
from . import crypto

from .net import *
from .utils import *
from .data_structures import *
from .config import *
from .crypto import *

class Client:

    def __init__(self, username, password, ip, port):
        self.username = username
        self.password = password
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def login(self):
        # Login
        packet = Packet()
        packet.packet_type = PacketType.LOGIN_REQUEST
        packet.add_data(LoginRequest(self.username, self.password))
        self.socket.send(packet.get_bytes())

    def get_file(self, file_name):
        packet = Packet()
        packet.packet_type = PacketType.GET
