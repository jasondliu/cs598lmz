import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib

default_path = os.path.join(os.path.expanduser('~'), '.local', 'share', 'icons', 'hicolor', '128x128', 'apps')

# Handle command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
args = parser.parse_args()

if args.debug:
    print('Debug mode enabled')

# Set up the database
if not os.path.exists(os.path.join(os.path.expanduser('~'), '.local', 'share', 'applications')):
    os.makedirs(os.path.join(os.path.expanduser('~'), '.local', 'share', 'applications'))

db_path = os.path.join(os.path.expanduser('~'), '.local', 'share',
