import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time
import datetime
import traceback
import json
import re
import logging

from . import utils
from . import sqliteutils
from . import config
from . import log
from . import exceptions
from . import settings
from . import platform
from . import version
from . import constants
from . import __version__


# TODO:
# - Add support for dbus signals
# - Add support for dbus properties
# - Add support for dbus methods
# - Add support for dbus interfaces
# - Add support for dbus objects
# - Add support for dbus names
# - Add support for dbus messages


#
# DBus types
#

class DBusType(object):
	def __init__(self, name, python_type, c_type, c_type_ptr, dbus_type, dbus_type_ptr, dbus_type_ptr_ptr, dbus_type_ptr_ptr_ptr):
		self.name = name
		self.python_type = python_type
		self.c_type
