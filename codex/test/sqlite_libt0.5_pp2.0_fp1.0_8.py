import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import subprocess
import time
import traceback
import logging

from . import utils
from . import config

_logger = logging.getLogger(__name__)


class DbusDaemon:
    """
    Dbus daemon thread.
    """

    def __init__(self, dbus_daemon_path, dbus_daemon_args, dbus_daemon_env):
        self.dbus_daemon_path = dbus_daemon_path
        self.dbus_daemon_args = dbus_daemon_args
        self.dbus_daemon_env = dbus_daemon_env
        self.process = None

    def start(self):
        """
        Start the dbus daemon.
        """
        _logger.debug("Starting dbus daemon")
