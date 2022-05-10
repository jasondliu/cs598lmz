import gc, weakref
import sqlite3
import string, logging, warnings
import sys, os, glob, shutil, tempfile
import collections, itertools

try:
    import thread
    import threading
    from threading import Lock, currentThread, Lock as _RLock
except ImportError:
    #  threading is only available in Python 2.4 or newer
    pass

import atexit
