import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# import sqlite3
# conn = sqlite3.connect('test.db')
# print "Opened database successfully";
# conn.close()

class simple_handler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname

    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname

    def process_IN_MODIFY(self, event):
        print "Modifying:", event.pathname

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("log.log", "a")
        self.log.write("\n")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra
