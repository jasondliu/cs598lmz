import ctypes
import ctypes.util
import threading
import sqlite3
import pickle

from Xlib.XK import string_to_keysym
from Xlib.display import Display
from Xlib import X

from Xlib.ext.xtest import fake_input
from Xlib import Xutil
from Xlib.ext import record, xinput

from PyQt4 import QtCore
from PyQt4.Qt import QThread
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QString, SIGNAL

from clint.textui import colored
from autokey import configdir

display = Display()
# keybindings table will be "keypresses"
conn = sqlite3.connect(configdir.data_dir + '/keypresses.sqlite')
c = conn.cursor()
keypressesTable = "keypresses";

# check if table exists
c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name=?''', (keypressesTable,))
# if not, create it
if len(c.fetchall()) == 0
