import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, fd, 0)

import os
import sys
import time
import traceback
import types

import pymongo

import config
import utils

class MongoDB(object):
    def __init__(self, dbname, host=None, port=None):
        self.dbname = dbname
        self.host = host or config.mongo_host
        self.port = port or config.mongo_port
        self.conn = None
        self.db = None
        self.connect()

    def connect(self):
        if self.conn is None:
            self.conn = pymongo.Connection(self.host, self.port)
        self.db = self.conn[self.dbname]

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
            self.db = None

    def __getattr__(self, name):
        if self.db is None:
            self.connect()
