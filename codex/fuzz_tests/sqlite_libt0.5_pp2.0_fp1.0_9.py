import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import struct

from . import _lib

class Error(Exception):
    pass

class NotFoundError(Error):
    pass

class Interface(object):
    """
    A network interface.
    """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s name=%r>' % (self.__class__.__name__, self.name)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self == other

    @property
    def mac_address(self):
        """
        The interface's MAC address.
        """
        return _lib.mac_address(self.name)

    @property
    def ipv4_address(self):
        """
        The interface's IPv4 address.
        """
        return _lib.ipv4_address(self
