import socket
import _thread
from threading import Thread, Lock
import sys
from pynput import keyboard, mouse

from config import *
from keys import *

from motion import Motion

from time import sleep
from random import randint
from datetime import datetime, timedelta


class Securityo(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.ruuning = True
        self.security()


