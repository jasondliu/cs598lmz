import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import logging
import time
import math
import traceback
import socket
import struct

# Third party libraries
import numpy
import psutil

# Our own stuff
import config
import sharedmem
import tty
import mdb
import util
import shm

class Plugin(threading.Thread):
    """
    Base class for plugins.
    """

    def __init__(self, name, config, queue, logger, **kwargs):
        """
        Initialize the plugin.
        """
        threading.Thread.__init__(self)
        self.name = name
        self.config = config
        self.logger = logger
        self.queue = queue
        self.shutdown = False
        self.debug = self.config.get("debug")

        # Create shared memory segment if it doesn't exist
        # TODO: move this to the main process
        # TODO: implement a lock
        if not os.path.exists(sharedmem.SHM_DIR):
            os.makedirs(sharedmem.SHM_DIR
