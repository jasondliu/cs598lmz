import ctypes
import ctypes.util
import threading
import sqlite3
import time

class FMOD_ERROR(ctypes.Structure):
    _fields_ = [
                ("error", ctypes.c_int),
                ]

class FMOD_STATE(ctypes.c_ushort):
    STOPPED = 0
    PLAYING = 1
    PAUSED = 2
    UNUSED = 3
    END = 4
   
class FMOD_RESULT(ctypes.c_int):
    OK = 0
    ERR_BADCOMMAND = -1
    ERR_CHANNEL_ALLOCATION = -2
    ERR_DMA = -3
    ERR_FILE_BAD = -4
    ERR_FILE_COULDNOTSEEK = -5
    ERR_FILE_DISKEJECTED = -6
    ERR_FILE_EOF = -7
    ERR_FILE_ENDOFDATA = -8
    ERR_FILE_NOTFOUND = -9
    ERR_FORMAT = -10
    ERR_HTTP = -11
