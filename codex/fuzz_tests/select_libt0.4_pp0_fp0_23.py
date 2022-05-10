import selectors
import socket
import types

#import os
#import sys
#import time

#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

#import config
#import log
#import log_handler
#import log_formatter

import config
import log
import log_handler
import log_formatter
import server_handler
import server_exception
import server_selector


class Server(object):
    """
    A server that accepts connections and dispatches them to a handler.
    """
    def __init__(self,
                 hostname,
                 port,
                 handler,
                 log_level=logging.DEBUG,
                 log_format=None,
                 log_file=None,
                 log_max_bytes=0,
                 log_backup_count=0,
                 log_encoding=None,
                 log_delay=False,
                 log_datefmt=None,
                 log_style='%',
                 log_name=None,
                 log_console=False
