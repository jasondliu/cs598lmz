import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/jmccown/runscons.sqlite3')
import simplejson as json
import traceback
import libevent



# Thread for libevent and sqlite3
class libeventSocketThread(threading.Thread):
    def __init__(self, host, username, password, dbconn):
        threading.Thread.__init__(self)
        self.host = host
        self.username = username
        self.password = password
        self.dbconn = dbconn
    def run(self):
        libevent_socket.init(self.host, self.username, self.password, self.dbconn)

class libevent_socket:
    def init(host, username, password, dbconn):
        thread_evbase = libevent.Base()
