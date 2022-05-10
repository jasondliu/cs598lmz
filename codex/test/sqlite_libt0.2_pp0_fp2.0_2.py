import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import subprocess
import re
import json
import traceback
import logging

from . import utils

logger = logging.getLogger(__name__)

class DBusError(Exception):
    pass

class DBusTimeoutError(DBusError):
    pass

class DBusConnectionError(DBusError):
    pass

class DBusSignalMatch(object):
    def __init__(self, bus, sender, path, interface, member, args):
        self.bus = bus
        self.sender = sender
        self.path = path
        self.interface = interface
        self.member = member
        self.args = args

    def __repr__(self):
        return '<DBusSignalMatch sender=%r path=%r interface=%r member=%r args=%r>' % (
            self.sender, self.path, self.interface, self.member, self.args)

