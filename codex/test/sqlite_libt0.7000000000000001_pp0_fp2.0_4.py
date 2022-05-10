import ctypes
import ctypes.util
import threading
import sqlite3
import sys

AVFORMAT_NOFILE = -1414092869

class AVFormatContext(ctypes.Structure):
    pass

class AVDictionaryEntry(ctypes.Structure):
    _fields_ = [("key", ctypes.c_char_p),
                ("value", ctypes.c_char_p)]

class AVIOContext(ctypes.Structure):
    pass

class AVCodecContext(ctypes.Structure):
    pass

class AVInputFormat(ctypes.Structure):
    pass

