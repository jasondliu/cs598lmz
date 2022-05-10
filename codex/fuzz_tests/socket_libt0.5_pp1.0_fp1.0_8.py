import socket
import sys
import time
import threading
import logging
import json
import math

from ws4py.client.threadedclient import WebSocketClient
from ws4py.manager import WebSocketManager

from sense_hat import SenseHat

if sys.version_info[0] < 3:
    import Queue as queue
else:
    import queue as queue


logging.basicConfig(level=logging.DEBUG)

# Connect to sensehat
sense = SenseHat()

# Setup websocket manager
manager = WebSocketManager()

# Connect to the websocket server
class DummyClient(WebSocketClient):
    def opened(self):
        logging.info("WebSocket opened")

    def closed(self, code, reason=None):
        logging.info("WebSocket closed")

    def received_message(self, m):
        logging.info("WebSocket received message")
        logging.debug(m)


ws = DummyClient('ws://localhost:8080/ws')
ws.connect()

# Setup the queue and start the thread
q = queue.
