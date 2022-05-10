import select
import socket
import sys
import threading

from . import common
from . import config
from . import log
from . import util

class Client(object):
    def __init__(self, host, port, username, password, database,
                 max_connections=None, max_idle_time=None,
                 connect_timeout=None, use_unicode=None, charset=None,
                 sql_mode=None, read_default_file=None, read_default_group=None,
                 cursorclass=None, init_command=None, connect_kwargs=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.max_connections = max_connections
        self.max_idle_time = max_idle_time
        self.connect_timeout = connect_timeout
        self.use_unicode = use_unicode
        self.charset = charset
        self.sql_mode = sql_mode
        self.read_
