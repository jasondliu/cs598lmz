import socket
import sys
import time
import threading
import Queue
import json
import random
import os
import subprocess
import datetime
import shutil
import re
import urllib2

#import pdb

#pdb.set_trace()

#-------------------------------------------------------------------------------
# Global variables
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Global functions
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Class definitions
#-------------------------------------------------------------------------------

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
