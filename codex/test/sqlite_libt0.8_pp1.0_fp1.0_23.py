import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import webbrowser

# load C library
_loc = ctypes.util.find_library("avcodec")
_loc = _loc.split(".")[0]
_loc = _loc.split("/")
_loc = "/".join(_loc[:-1]+["libavcodec.so.57"])
_loc = ctypes.util.find_library("avcodec")

try:
    libavcodec=ctypes.cdll.LoadLibrary(_loc)
except:
    _loc = ctypes.util.find_library("avcodec")
    libavcodec=ctypes.cdll.LoadLibrary(_loc)

# encoder settings
CODEC_ID_MPEG4=13
CODEC_ID_FLV1=22
CODEC_ID_VP8=136
CODEC_ID_VP9=167

# get library functions
avcodec_version = libavcodec.avcodec_version
avcodec_version.restype = ctypes.c_uint
