import ctypes
import ctypes.util
import threading
import sqlite3
import time
import traceback
import os
import sys

class NetworkError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class CServer:
    def __init__(self):
        self.m_socket = socket.socket()
        self.m_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.m_networkLock = threading.Lock()
        self.m_thread = None
        self.m_pool = None
        self.m_port = None
        self.m_threads = []
        self.m_shutdown = False
        self.m_clients = []
        self.m_handlers = {}
        self.m_sqliteLock = threading.Lock()
        self.m_sqliteQueue = []
        self.m_sqliteInProgress = False
        self.m_sqliteThread = None
        self.m_sqlite =
