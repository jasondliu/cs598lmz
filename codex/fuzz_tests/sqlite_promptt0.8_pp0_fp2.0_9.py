import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
DB_FILE = "proxies.db"
conn = sqlite3.connect(DB_FILE)
c = conn.cursor
c.execute("CREATE TABLE proxies (ip text, port text, country text, anon text, type text, speed int)")

libc = ctypes.CDLL(ctypes.util.find_library('c'))

import sys
import os
import select
import socket
import threading
import SocketServer
import fcntl
import time
import signal
import getopt
import string
import re

# constants
CON_CLOSED = 0
CON_OPEN = 1
CON_REQUEST = 2
BYTES_TO_READ = 10240

TIMEOUT = 10

# global variables
listen_port = 80

# debug options
debug = 0
debug_data = 0


class ThreadingServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):

    allow_reuse_address = True
    daemon_threads = True

    def handle_error(self, request, client_address):
        #
