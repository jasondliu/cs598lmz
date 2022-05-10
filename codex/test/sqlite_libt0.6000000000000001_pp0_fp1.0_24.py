import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import traceback
import itertools
import config
import random
import json

from datetime import datetime
import random

from collections import namedtuple

from pydbus import SessionBus, SystemBus, BusType
from gi.repository import GLib

from . import dbus_types
from . import dbus_constants
from . import dbus_helpers

from .dbus_types import *
from .dbus_constants import *
from .dbus_helpers import *

class DBusSignalFilter(object):
    def __init__(self, interface, member, object_path, bus_name=None):
        self.interface = interface
        self.member = member
        self.object_path = object_path
        self.bus_name = bus_name

class DBusSignalFilterList(object):
    def __init__(self):
        self.filters = []

    def add(self, filter):
        self.filters.append(filter)

