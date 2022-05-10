import ctypes
import ctypes.util
import threading
import sqlite3

import pygeoip

__all__ = ['load_extension', 'GeoIP', 'FIELD_ADDR', 'FIELD_DOMAIN',
           'FIELD_HOST', 'FIELD_ID', 'FIELD_PATH', 'FIELD_TYPE',
           'MAX_ADDRESS_LENGTH', 'MAX_LOCATION_STRING_LENGTH',
           'TYPE_ADDR', 'TYPE_HOST', 'TYPE_NONE', 'TYPE_PATH',
           'TYPE_URL']

# Load the C extension module and get the interface version
try:
    import tor_ext
    assert tor_ext.get_interface_version() >= 3
except (ImportError, AssertionError):
    raise ImportError('Could not load the Python C extension '
                      'module "tor_ext".')

# Initialise the per-thread GeoIP database
_geoip_lock = threading.Lock()
_geoip_data = sqlite3.connect(':memory:')
_geoip_data.row_factory = sqlite3.Row
_geoip_data
