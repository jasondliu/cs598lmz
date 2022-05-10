import socket
import json

from websocket_server import WebsocketServer

from threading import Thread

import time

from logger import log

from client import Client

class Server:
	def __init__(self, port=18000):
		self.port = port
		self.clients = []
		self.client_map = {}
		self.server = None
		self.running = False
		self.thread = None

	def start(self):
		log("Starting server...")
		self.server = WebsocketServer(self.port, host='0.0.0.0')
		self.server.set_fn_new_client(self.on_new_client)
		self.server.set_fn_client_left(self.on_client_left)
		self.server.set_fn_message_received(self.on_message_received)
		self.server.run_forever()

	def on_new_client(self, client, server):
		log("New client connected!")

