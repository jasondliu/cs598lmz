import ctypes
import ctypes.util
import threading
import sqlite3
import binascii
import json
import subprocess
import os
import struct
import time
import pickle
import logging

log = logging.getLogger('frida')

_user_agent = "Frida/%s" % __version__


class FileNotFoundError(Exception):
    pass


class InvalidArgumentError(Exception):
    pass


class ProcessNotFoundError(Exception):
    pass


class TimeoutError(Exception):
    pass


class ProcessDetachedError(Exception):
    pass


class InterruptedError(Exception):
    pass


class DuplicateReceiveError(Exception):
    pass


class ExportedSymbolError(Exception):
    pass


class NotEnabledError(Exception):
    pass


class NotEnrolledError(Exception):
    pass


class ModuleNotFoundError(Exception):
    pass


class SessionClosedError(Exception):
    pass


class ObsoleteDeviceError(Exception):
    pass


class ScriptClosedError(Exception):
    pass


class _MessageWriter(object):
    def __init
