import socket, select
from threading import Thread
from time import sleep
from protocol import *
from bot import *
from server import *
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

class Client(Thread):
	def __init__(self, name, host, port, account, password, *args, **kwargs):
		super(Client, self).__init__(*args, **kwargs)
		self.daemon = True
		self.name = name
		self.host = host
		self.port = port
		self.account = account
		self.password = password
		self.server = Server(host, port)
		self.bot = Bot()

	def start(self):
		super(Client, self).start()
		logger.debug("Starting client thread.")

	def run(self):
		self.bot.start()

