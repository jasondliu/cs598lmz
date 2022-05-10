import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time
import signal

class NetLogger(object):
    def __init__(self, database_name, seccomp_file=None, version=None,
                 timeout=None, sql_log_size=10000, max_log_size=None):
        self.logger = logging.getLogger('NetLogger')
        self.logger.setLevel(logging.DEBUG)
        self.sql_log_size = sql_log_size
        self.timeout = timeout
        self.max_log_size = max_log_size
        self.database_name = database_name
        if seccomp_file is None:
            self.seccomp_file = "seccomp_bpf.h"
        else:
            self.seccomp_file = seccomp_file
        self.version = version
        self.lock = threading.RLock()

    def initialize(self):
        """Initializes the logger.  This will create a database connection,
        create the database tables if needed, and start a logging thread."""
       
