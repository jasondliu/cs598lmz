import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import os
import sys
import time
import traceback
import logging
import logging.handlers
import logging.config
import ConfigParser
import subprocess

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk, GLib

import lib.common
import lib.config
import lib.db
import lib.i18n
import lib.file_monitor
import lib.notify
import lib.notify_watcher
import lib.queue
import lib.task
import lib.task_manager
import lib.task_watcher
import lib.task_runner
import lib.window
import lib.window_trayicon
import lib.window_preferences
import lib.app_indicator
import lib.app_indicator_menu
import lib.app_indicator_watcher

#import glib

#import pynotify

#import dbus
#import dbus.service
#import dbus.main
