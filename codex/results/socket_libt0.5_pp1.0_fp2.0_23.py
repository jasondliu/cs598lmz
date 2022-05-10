import socket
import struct
import sys
import time
import threading
import Queue

#
# Class to handle the communication with the server
#
class Client(object):

    #
    # Initialize the Client
    #
    def __init__(self, ip, port, game_name, game_id, game_size, game_type, game_time, game_creator, game_password):
        self.ip = ip
        self.port = port
        self.game_name = game_name
        self.game_id = game_id
        self.game_size = game_size
        self.game_type = game_type
        self.game_time = game_time
        self.game_creator = game_creator
        self.game_password = game_password
        self.socket = None
        self.queue = Queue.Queue()
        self.lock = threading.Lock()
        self.running = False
        self.buffer = ""
        self.connected = False
        self.thread = None

    #
    # Connect to the server
    #
   
