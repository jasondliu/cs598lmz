import ctypes
import ctypes.util
import threading
import sqlite3

from . import util

_libmpv = None


class ConfigOption:
    def __init__(self, mpv, name):
        self.mpv = mpv
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.get_property(self.name)

    def __set__(self, instance, value):
        instance.set_property(self.name, value)


def _get_libmpv():
    global _libmpv

    if _libmpv is not None:
        return _libmpv

    name = ctypes.util.find_library("mpv")
    if name is None:
        raise OSError("can't find libmpv")

    _libmpv = ctypes.CDLL(name)

    return _libmpv


class MPV(object):
    def __init__(self, log_handler=None, log_level="info", **kwargs):
        """Create an instance of the MPV player."""
