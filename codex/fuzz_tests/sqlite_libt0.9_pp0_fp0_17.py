import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import re
import inspect
from cStringIO import StringIO
import urllib2
import threading

try:
    import faulthandler
except ImportError:
    faulthandler = None

libemacspeak = ctypes.CDLL(ctypes.util.find_library('emacspeak'))

dll_types = {
    'cmp': ctypes.c_int,
    'tts_say': ctypes.c_int,
    'tts_enqueue': ctypes.c_int,
    'tts_enqueue_silence': ctypes.c_int,
    'tts_enqueue_character': ctypes.c_int,
    'tts_enqueue_commas': ctypes.c_int,
    'tts_chunk_and_enqueue': ctypes.c_int,
    'tts_stop': ctypes.c_int,
    'tts_stop_immediately': ctypes.c_int,
    'tts_is_running
