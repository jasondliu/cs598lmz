import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('c:\\temp\\test.sqlite3')

WTS_CURRENT_SERVER_HANDLE = 0

WTS_CURRENT_SESSION = 0x4

WTS_SESSION_LOCK = 0x7
WTS_SESSION_UNLOCK = 0x8

WTS_CONSOLE_CONNECT = 0x1
WTS_CONSOLE_DISCONNECT = 0x2
WTS_REMOTE_CONNECT = 0x3
WTS_REMOTE_DISCONNECT = 0x4
WTS_SESSION_LOGON = 0x5
WTS_SESSION_LOGOFF = 0x6
WTS_SESSION_REMOTE_CONTROL = 0x9

WTS_INFO_CLASS = dict((x, x) for x in dir(ctypes.windll.Wtsapi32) if x.startswith("WTS"))

WTS_EVENT = {
    WTS_CONSOLE_CONNECT: "Console connect",
    WTS_CONSOLE_DISCONNECT: "Console disconnect",
    WTS
