import ctypes
import ctypes.util
import threading
import sqlite3
import os

__version__ = '2.0.0'

try:
    from pkg_resources import get_distribution, DistributionNotFound
    try:
        __version__ = get_distribution(__name__).version
    except DistributionNotFound:
        # package is not installed
        pass
except ImportError:
    # package is not installed
    pass

class ExifTool(object):
    """
    Encapsulates ExifTool executable as a Python object
    """

    _executable = 'exiftool'

    _executable_search_paths = [
        '/usr/local/bin',
        '/usr/bin'
    ]

    _encoding = 'utf-8'

    # OS and library
    _libc_name = ctypes.util.find_library('c')
    _libc = ctypes.CDLL(_libc_name)
    _system = _libc.system

    # Path to exiftool executable
    _exiftool_path = None

    # Lock for writing/reading to STDIN/STDOUT/ST
