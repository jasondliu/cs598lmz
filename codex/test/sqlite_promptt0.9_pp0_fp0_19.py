import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect >= 3.6.7 or 3.7.0
if sqlite3.version < '3.6.7':
    raise NotImplementedError('Your pysqlite2 package is old'
            ', please upgrade to the latest version')
try:
    import new
except ImportError:
    import types as new

import riak.transports.mock as mock
from riak.transports import pbc


def get_site_packages():
    """
    Returns the list of user-defined site-packages directories
    """
    import sys
    if sys.platform == 'win32':
        site_packages = []
        from distutils.sysconfig import get_python_lib
        for p in list(sys.path):
            if p.lower().endswith('site-packages'):
                site_packages.append(p)
        site_packages.append(get_python_lib())
    else:
        from distutils.sysconfig import get_python_lib
        site_packages = [get_python_lib()]
    return site_packages

