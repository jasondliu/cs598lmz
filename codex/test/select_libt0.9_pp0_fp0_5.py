import selectors, sys, json
from time import time
from threading import Thread
from queue import Queue
import numpy as np
from models import *
import warnings

#x_train.shape
#y_train.shape
#x_test.shape
#y_test.shape
warnings.filterwarnings("ignore", category=DeprecationWarning)

class Server:
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.host="localhost"
        self.port="3586"        
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.bind((self.host, int(self.port)))
        
        self.message_q = Queue()
        self.lsock.listen()
        print("listening on", (self.host, int(self.port)))
        self.lsock.setblocking(False)
        #self.sel.register(self.lsock, selectors.EVENT_READ)
        self.sel.register
