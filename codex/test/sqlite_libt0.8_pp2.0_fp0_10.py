import ctypes
import ctypes.util
import threading
import sqlite3
import os
import re
import time
import sys
import traceback
import tempfile
import logging
import os.path
import platform
import subprocess
import shutil
from xml.dom.minidom import parse
import xml.dom.minidom
import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib


class Configs(object):
    work_dir = os.path.expanduser("~/.deepin-system-monitor")
    config_file = os.path.join(work_dir, "deepin-system-monitor.conf")
    session_file = os.path.join(work_dir, "deepin-system-monitor.session")
    task_schema = os.path.join(work_dir, "task-schema.xml")
    task_file = os.path.join(work_dir, "task-config.xml")


class I18N(object):

    def __init__(self, domain, path):
        self.domain = domain
        self.path
