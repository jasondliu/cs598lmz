import ctypes
import ctypes.util
import threading
import sqlite3
import time

import os
import os.path
import sys

import struct

import array
import socket

import platform
import Queue
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class SQLiteDB():
    def __init__(self, file):
        self.file = file
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            self.cursor = None
        self.connection = sqlite3.connect(self.file)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        self.cursor = None
        self.connection = None

    def execute(self, sql, params=None):
        if self.connection is None:
            self.connect()
        if params is None:
            self.cursor.execute(sql)
