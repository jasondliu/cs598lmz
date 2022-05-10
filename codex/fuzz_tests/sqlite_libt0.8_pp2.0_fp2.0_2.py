import ctypes
import ctypes.util
import threading
import sqlite3
import time

PHONE_DB = "/home/user/.local/share/system/privileged/TelephonyProvider/databases/mmssms.db"
SQL_QUERY = "select * from sms where type = 1 and date between %d and %d order by date"

# Create a new condition
condition = threading.Condition()
# Set up the lib
libnotify = ctypes.CDLL(ctypes.util.find_library("notify"))

# Set up the arguments and return types
libnotify.notify_init.restype = ctypes.c_int
libnotify.notify_init.argtypes = [ctypes.c_char_p]

libnotify.notify_notification_new.restype = ctypes.c_void_p
libnotify.notify_notification_new.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]

libnotify.notify_notification_show.restype = ctypes.c_int
lib
