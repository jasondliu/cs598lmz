import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import log
from . import protocol
from . import util

class Server(threading.Thread):
    def __init__(self, host, port, config_file, log_file, log_level,
                 log_format, log_date_format, max_connections,
                 max_connections_per_ip, max_messages_per_second,
                 max_messages_per_second_per_ip,
                 max_simultaneous_connections_per_ip,
                 max_simultaneous_connections_per_ip_window,
                 connection_timeout, ping_interval, ping_timeout):
        threading.Thread.__init__(self)
        self.daemon = True

        self.host = host
        self.port = port
        self.config_file = config_file
        self.log_file = log_file
        self.log_level = log_level
        self.log_format = log_
