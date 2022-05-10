import ctypes
import ctypes.util
import threading
import sqlite3

DEFAULT_DATABASE = '~/.pympd.db'

def _load_mpd_source():
    mpd_module = None
    mpd_module_name = ctypes.util.find_library('mpd')
    if mpd_module_name:
        try:
            mpd_module = ctypes.CDLL(mpd_module_name)
            if not mpd_module:
                raise ValueError('Could not load MPD DLL')
        except ValueError as e:
            print(e)
    return mpd_module

class _MpdValuePointer(ctypes.c_void_p):
    def get_value(self):
        return bool(self.value)

class MPDRealtime(object):
    def _get_isplaying(self):
        return self.mpd.mpd_innards[20] < 3
    isplaying = property(fget=_get_isplaying)

