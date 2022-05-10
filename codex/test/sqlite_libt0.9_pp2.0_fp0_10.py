import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import uuid

from . import modname, bindir, libdir, include_headers
from .resource_loader import ResourceLoader
from .config import *

# In case we don't find the lib, this list is used to print possible locations
# It is assumed the lib is installed in $prefix/bin/mod_wsgi/lib/libmod_wsgi.so
# This is based on test code code from http://trac.edgewall.org/browser/trunk/tractags/tractags/api.py

_possible_locations = set()

if sys.platform.startswith('linux'):
    # Debian.
    _possible_locations = set([
        '/usr/lib/apache2/modules/mod_wsgi.so',
    ])
    # Fedora.
