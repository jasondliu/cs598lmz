import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn=sqlite3.connect('test.db')
#print "Opened database successfully";
#conn.close()

import re
import time
import datetime
import json
import urllib2
import urllib
import sys
import os
import subprocess

import pycurl
import StringIO

import lib.config
import lib.log
import lib.utils
import lib.db
import lib.http

#
# Globals
#
_log = lib.log.logger("syslog")
_log.setLevel(lib.log.DEBUG)

#
#
#
class Syslog:
    """Syslog class"""
    def __init__(self, config):
        """
        Initialize syslog class
        """
        self.config = config
        self.db = lib.db.db(config)
        self.http = lib.http.http(config)
        self.log = lib.log.logger("syslog")
        self.log.setLevel(lib.log.DEBUG)
