import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import random
import socket
import time
import string
import subprocess
import os
import shutil

# The directory where the configuration file is stored.
#
# In the case of a Unix-like system, this is:
# /home/$USER/.config/
#
# On Windows, this is:
# C:\\Users\\$USER\\AppData\\Roaming\\
#
# The configuration file is named 'config.db'
CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config')

# The version of the application.
VERSION = "0.9.3.3"

# The name of the SQLite configuration database.
CONFIG_FILE = "config.db"

# The name of the SQLite connection database.
CONNECTION_FILE = "connections.db"

# The name of the SQLite database for the connection history.
HISTORY_FILE = "connections.db"

# The name of the SQLite database for the port forwarding.
PORTFORWARD_FILE = "portforward.db"

# The
