import socket
import re
import os
import urllib
import urllib.parse
import threading
import signal
import logging

class WebServer:
    def __init__(self,PORT=8888,ROOT=os.getcwd()):
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.PORT = PORT
        self.ROOT = ROOT
        self.PORT = 8888
        self.ROOT = os.getcwd()
        self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.Sock.bind(('', self.PORT))
        self.Sock.listen(5)
        connectionContainer = threading.Thread(name='connectionContainer',target=self.connectionContainer)
        connectionContainer.start()
        logging.info('Server started on' + ' ' + str(self.PORT) + ' ' +
