import selectors
import socket
import threading
import time
import queue

from utils import *
from peer_protocol import *

class Peer(object):
    def __init__(self, thread_id, address, port, torrent):
        self.thread_id = thread_id
        self.address = address
        self.port = port
        self.torrent = torrent
        self.peer_id = None
        self.state = None
        self.connecting = False
        self.connected = False
        self.choked = True
        self.interested = False
        self.last_message = None
        self.last_time = 0
        self.last_download_time = 0
        self.last_upload_time = 0
        self.last_download_speed = 0
        self.last_upload_speed = 0
        self.download_speed = 0
        self.upload_speed = 0

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setblocking(0)
        self.select
