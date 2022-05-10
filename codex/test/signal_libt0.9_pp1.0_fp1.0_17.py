import signal
signal.signal(signal.SIGINT,signal.SIG_DFL)

import socket
import sys
#import thread
#import _thread
import threading
from struct import *
import select
import os
import time
import cv2
import numpy as np
from numpy.linalg import inv

#sys.path.append('/usr/local/lib/python3.5/dist-packages')
sys.path.append(os.path.join(os.path.dirname(__file__), '../include'))
from encdec import *
#from my_mode import *

#def thread():
#    print("ok")

class Walker(threading.Thread):
    def __init__(self, servo, camera, s):
        threading.Thread.__init__(self)
        self.servo = servo
        self.camera = camera
        self.s = s
        self.status = ""
        self.sock_lock = threading.Lock()
        self.sock_lock.acquire()
