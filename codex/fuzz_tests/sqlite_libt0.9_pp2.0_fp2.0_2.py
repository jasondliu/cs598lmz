import ctypes
import ctypes.util
import threading
import sqlite3 as sqlite


class ColorTerminal:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @classmethod
    def blue(cls, msg):
        return "%s%s%s" % (cls.OKBLUE, msg, cls.ENDC)

    @classmethod
    def green(cls, msg):
        return "%s%s%s" % (cls.OKGREEN, msg, cls.ENDC)

    @classmethod
    def yellow(cls, msg):
        return "%s%s%s" % (cls.WARNING, msg, cls.ENDC)

    @classmethod
    def red(cls, msg):
        return "%s%s%s" % (cls.FAIL, msg, cls.ENDC)

    @classmethod
    def pink
