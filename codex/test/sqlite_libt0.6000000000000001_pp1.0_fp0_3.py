import ctypes
import ctypes.util
import threading
import sqlite3
import signal
import os.path
import sys
import logging

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


def get_db_filename():
    home_folder = os.path.expanduser('~')
    return os.path.join(
        home_folder,
        '.local',
        'share',
        'gnome-shell',
        'extensions',
        'gnome-shell-extension-autohidetopbar@gnome-shell-extensions.gcampax.github.com',
        'db.sqlite'
    )


