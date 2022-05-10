import socket
from threading import Thread
from time import sleep
from Tkinter import *

from libs.config import *
from libs.functions import *
from libs.logger import *
from libs.motd import *
from libs.networking import *
from libs.networking import *
from libs.pinger import *
from libs.screen_manager import *
from libs.text_manager import *
from libs.user_manager import *
from libs.window_manager import *


class Client:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.root = Tk()
		self.screen_manager = ScreenManager(self.root)
		self.window_manager = WindowManager(self.root, self.screen_manager)
		self.text_manager = TextManager(self.root)
		self.user_manager = UserManager()
		self.networking = Networking(self)
