import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect. Check wiring in pcduino.IOError.
from sqlite3 import OperationalError
from sqlite3 import (Error, Warning, InterfaceError, DatabaseError,
                     DataError, OperationalError, IntegrityError, InternalError,
                     ProgrammingError, NotSupportedError)

# Definition of HookEvent
_MOUSEEVENTF_MOVE         = 0x0001 # mouse move
_MOUSEEVENTF_LEFTDOWN     = 0x0002 # left button down
_MOUSEEVENTF_LEFTUP       = 0x0004 # left button up
_MOUSEEVENTF_RIGHTDOWN    = 0x0008 # right button down
_MOUSEEVENTF_RIGHTUP      = 0x0010 # right button up
_MOUSEEVENTF_MIDDLEDOWN   = 0x0020 # middle button down
_MOUSEEVENTF_MIDDLEUP     = 0x0040 # middle button up
_MOUSEEVENTF_ABSOLUTE     = 0x8000 # absolute move
PRESSED = 1
RELEASED = 0
# Def
