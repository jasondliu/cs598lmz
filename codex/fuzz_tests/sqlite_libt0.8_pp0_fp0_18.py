import ctypes
import ctypes.util
import threading
import sqlite3
import ssl
import os
import signal
import subprocess

import dbus
import dbus.mainloop.glib

import gi
gi.require_version("GError", "0.0")
from gi.repository import GError

import time

import utils
import pytz

_DBUS_SIGNATURE_JSON = utils._DBUS_SIGNATURE_JSON

(DBUS_START_REPLY_SUCCESS,
DBUS_START_REPLY_ALREADY_RUNNING) = range(2)

(DBUS_NAME_FLAG_ALLOW_REPLACEMENT = 0x1,
DBUS_NAME_FLAG_REPLACE_EXISTING = 0x2,
DBUS_NAME_FLAG_DO_NOT_QUEUE = 0x4)

(DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER,
DBUS_REQUEST_NAME_REPLY_IN_QUEUE,
DBUS_REQUEST_NAME_REPLY_EXISTS
