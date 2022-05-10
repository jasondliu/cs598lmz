import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import unicodedata

# macOS
framework_path = ctypes.util.find_library('CoreFoundation')
objc = ctypes.cdll.LoadLibrary(framework_path)

# Linux
#objc = ctypes.CDLL('libobjc.so.4')

# Windows
#objc = ctypes.CDLL('libobjc.dll')


class PathMonitor(object):
    def __init__(self, path, callback):
        """
        An abstract class that watches the specified path and calls the
        callback method when the file is modified, deleted or created.

        The callback method should take a single parameter that is a tuple of
        exactly two values: (path, event)

        The path value is always the one passed to the constructor, even in the
        case of a file being moved or renamed.

        The event is a string, the value of which is determined by the
        specific PathMonitor subclass:
        'delete' - the file has been deleted
        'rename' - the file has been renamed or moved (the old file no longer
           
