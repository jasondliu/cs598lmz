import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#import _sqlite3

#-----------------------------------------------------------------------------

__author__ = "Jorge Niedbalski R. <jnr@metaklass.org>"
__version__ = "0.0.1"
__license__ = "GNU GPL v3"

#-----------------------------------------------------------------------------

# Python 2.x backward compatibility
try:
    input = raw_input
except NameError:
    pass

class CursesUI:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.running = True
        self.maxy, self.maxx = self.stdscr.getmaxyx()

        self.conn = sqlite3.connect('/var/tmp/log.db')
        self.c = self.conn.cursor()

        self.stdscr.timeout(1000)


    def search(self, data):
        self.c.execute("SELECT * FROM log WHERE log LIKE ?", ('%'+data+'%',))
        res = self.c.fetchall()
        if not res
