import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect.

# Database related variables
DB_NAME = "C:/Users/natha/Documents/Programming/python/git/sqliteTest/sqlite_windows/test.db"
TABLE_NAME = "test"

# Speech related variables
SPEECH_LIBRARY = "speak.dll"
SPEECH_LIBRARY_DLL = ctypes.util.find_library(SPEECH_LIBRARY)
SPEECH_DLL = ctypes.cdll.LoadLibrary(SPEECH_LIBRARY_DLL)
SPEECH_VOICE = -1
SPEECH_VOLUME = 100
SPEECH_RATE = 0
SPEECH_PITCH = 5
lib_thread = None

class Test(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.db = None
        self.busy = False
        self.threads = []

    @Slot(str)
    def fn_Test(self, txt):
        print(txt)

    @Slot(str)
   
