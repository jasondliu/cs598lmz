import select
import socket
import sys
import time
import logging
import threading
import Queue
import struct
import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from common import *

#TODO: Make this configurable
HOST = '192.168.0.1'
PORT = 21
USERNAME = 'test'
PASSWORD = 'test'

class FTPThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        # Instantiate a dummy authorizer for managing 'virtual' users
        authorizer = DummyAuthorizer()

        # Define a new user having full r/w permissions and a read-only
        # anonymous user
        authorizer.add_user(USERNAME, PASSWORD, os.getcwd(), perm='elradfmwM')
