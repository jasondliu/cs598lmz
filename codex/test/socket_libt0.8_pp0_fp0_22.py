import socket
import ssl
import threading
import time

from config import Config
from wallet import Wallet

class Server(object):
    def __init__(self):
        self.host = Config.host
        self.port = Config.port
        self.ssl = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
        self.ssl.load_cert_chain(certfile="server.crt",keyfile="server.key")
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket = self.ssl.wrap_socket(self.socket)
        self.socket.bind((self.host,self.port))
        self.listening = True
        self.wallets = {}
        self.lock = threading.Lock()
        self.ping_time = 1
        self.ping_messages = {}
        self.ping_responses = {}
        self.continue_thread = threading.Event()
        self.continue_thread.set()
        self.server_
