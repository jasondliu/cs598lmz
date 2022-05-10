import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import io
import requests

import pyasn

class ACL(object):
    def __init__(self, dbpath):
        self.db = sqlite3.connect(dbpath)
        self.cur = self.db.cursor()

