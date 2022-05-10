import ctypes
import ctypes.util
import threading
import sqlite3
import os
import configparser
import datetime
import time
import json

class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def get_conf():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    return config


def get_logger(name):
    import logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('./log/' + name + '.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def
