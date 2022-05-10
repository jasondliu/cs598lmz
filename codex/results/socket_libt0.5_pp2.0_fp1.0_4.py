import socket
import sys
import time
import os
import threading
import logging
import json
#import pysqlite2.dbapi2 as sqlite
import sqlite3 as sqlite
import shutil

#from pyftpdlib.authorizers import DummyAuthorizer
#from pyftpdlib.handlers import FTPHandler
#from pyftpdlib.servers import FTPServer

import ftp_server
import ftp_client
import ftp_common

import ftp_sync

import ftp_config

from ftp_config import *

def get_free_port(start_port):
    port = start_port
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind(('127.0.0.1', port))
        except socket.error:
            port += 1
            continue
        break
    s.close()
    return port

class ftp_thread(threading.Thread):
    def __init__(self, name, server, port
