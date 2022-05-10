import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect performance
from time import sleep, time
from random import randint
from multiprocessing import Pool

from shutil import rmtree
from os import listdir, makedirs, remove
from os.path import isfile, join, exists, dirname

from . import *

class TestPyglet(unittest.TestCase):
    def test_pyglet(self):
        '''
        Pyglet:
            version: 2.0.0
            backend: SDL2
            platform: Darwin-17.7.0-x86_64-i386-64bit
        '''
        self.assertTrue(pyglet.version[0] == 2)

    def test_threading(self):
        '''
        threading.get_ident()
            => <class 'int'>
        '''
        self.assertTrue(type(threading.get_ident()) == int)

