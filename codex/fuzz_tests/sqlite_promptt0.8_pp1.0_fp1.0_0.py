import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
assert sqlite3.connect(':memory:')
# Test sqlite3.enable_load_extension
conn = sqlite3.connect(':memory:')
conn.execute('pragma compile_options')
try:
    # Python 3.8.0+
    from sqlite3 import enable_load_extension  # noqa: F401
except ImportError:
    # Python 3.7.4-
    enable_load_extension = conn.enable_load_extension

enable_load_extension(True)
try:
    # Python 3.8.0+
    conn.load_extension('mod_spatialite')
except AttributeError:
    # Python 3.7.4-
    conn.load_extension('mod_spatialite', 'sqlite3_modspatialite_init')

# Test loading libspatialite, libspatialite.so
libname = ctypes.util.find_library('spatialite')
libspatialite = ctypes.CDLL(libname)
# Test loading libspatialite, lib
