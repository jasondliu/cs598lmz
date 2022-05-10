import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect only -> some library not found
#import sqlite3.dbapi2 as sqlite3


version = '2.5'

# Set debug flag depending on zip
if __file__.startswith('/usr/'):
    debug = False
    platform = 'a'
else:
    debug = True
    platform = 'w'

# Set true is there is a smartphone
smartphone = False

# this is the default configuration string for the library.
# it will be send to the library for each launched process
lib_config = "noautoreset;timeout=30000;\
    serialreadtimeout=150;serialpassthrusleeptime=50;serialpassthrutimeout=250;\
    serialpassthruignorenack=yes;serialpassthru=yes"

# HID and com errors
hid_errors = {
    0: "",
    1: "bad header",
    2: "bad packet UTF",
    3: "unknown command",
    4: "bad packet CKS",
    5: "no memory",
    6: "
