import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime
import traceback
import subprocess
import re
import socket
import select
import fcntl
import errno
import signal
import logging

from . import utils
from . import config
from . import database
from . import constants
from . import logger
from . import exceptions
from . import __version__

log = logging.getLogger(__name__)

#
# This is the main class that does all the work.
#
class Monitor(object):
    #
    # Initialize the monitor.
    #
    def __init__(self, args):
        self.args = args
        self.config = config.Config(args.config)
        self.database = database.Database(self.config)
        self.logger = logger.Logger(self.config)
        self.log_file = None
        self.log_file_lock = threading.Lock()
        self.log_file_name = None
        self.log_file_name_lock = threading.Lock()
        self.
