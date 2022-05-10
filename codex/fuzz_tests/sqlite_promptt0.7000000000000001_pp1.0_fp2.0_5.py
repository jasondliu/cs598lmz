import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db').cursor().execute('CREATE TABLE test (a, b)')

import queue
import pdb
import traceback

import sys

# In some versions of py2exe code, we need to make sure to import this
import collections

try:
    from twilio.rest import TwilioRestClient
except ImportError:
    pass

import time

# Try to import pyzmq
try:
    import zmq
except ImportError:
    zmq = None

try:
    import dbus
    import dbus.service
    import dbus.mainloop.glib
    import gobject
    HAVE_DBUS = True
except ImportError:
    HAVE_DBUS = False

if sys.platform.startswith('win'):
    WINDOWS = True
else:
    WINDOWS = False

try:
    import serial
    HAVE_SERIAL = True
except ImportError:
    HAVE_SERIAL = False

try:
    import pyserial
    HAVE_PYSERIAL = True
except
