import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#  conn = sqlite3.connect('/home/randy/applications/sog/sog_conf.db')
#  c = conn.cursor()
#  c.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='sog_parameters';")
#  print c.fetchall()
#  conn.close()

import platform

if platform.system() == 'Windows':
  import msvcrt
  import os
  # Need to specify MSVCRT and not MSVCR100
  msvcrt.setmode(0, os.O_BINARY)
  msvcrt.setmode(1, os.O_BINARY)
  msvcrt.setmode(2, os.O_BINARY)
class DummyFile(object):
    def write(self, x): pass

def hide_console_on_start():
    '''
    Stops console window from appearing on Windows platforms
    '''
    if platform.system() == 'Windows':
        import ctypes
       
