import ctypes
import ctypes.util
import threading
import sqlite3
import random
import time
import sys
import os
import paramiko as ssh
import errno
import re
from datetime import datetime
from optparse import OptionParser
from kazoo.client import KazooClient
from collections import deque

zkhostport = "127.0.0.1:2181"
zkRoot = "/search-db-service/"
db_dir = "./"
db_node_dir = db_dir + "db/"
db_data_dir = db_node_dir + "data/"

request_queue = deque()

class SSHSession(ssh.SSHClient):
    """
    A simple wrapper of paramiko.SSHClient
    """
    def __init__(self, host, port, user, private_key, key_filename, **kwargs):
        super(SSHSession, self).__init__()
        self.set_missing_host_key_policy(ssh.client.AutoAddPolicy())
