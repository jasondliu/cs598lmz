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

