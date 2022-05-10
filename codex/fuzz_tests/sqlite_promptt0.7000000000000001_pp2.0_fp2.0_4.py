import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

def encode(s):
    return s.encode("utf-8")

class XdgMime(object):
    def __init__(self):
        self.lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("gio-2.0"))
        self.lib.g_content_type_get_mime_type.restype = ctypes.c_char_p
        self.cache = {}

    def get_mime_type(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            if isinstance(key, bytes):
                skey = key
            else:
                skey = key.encode("utf-8")
            ret =  self.lib.g_content_type_get_mime_type(skey)
            ret = ret.decode("utf-8")
            self.cache[key] = ret
            return ret

class FdWalker(threading.Thread):
    def __init__(self, path
