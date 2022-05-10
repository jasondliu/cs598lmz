import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import pprint
# PPrint module

# Test that all needed modules are present.
if not hasattr(ctypes, 'CDLL'):
    raise RuntimeError('Ctypes module has no attribute CDLL. Cannot continue.')

if not hasattr(ctypes.util, 'find_library'):
    raise RuntimeError(
        'Ctypes.util module has no attribute \'find_library\'. Cannot continue.')
# Test for library/lv2 support.
if not hasattr(ctypes, 'c_string_p'):
    raise RuntimeError('Ctypes module has no attribute \'c_string_p\'. Cannot continue.')

spice_lib = ctypes.CDLL(ctypes.util.find_library('spice'))
lv2_lib = ctypes.CDLL(ctypes.util.find_library('lv2'))
indexed_list = []
patch_list = []
thread_list = []

#glib.g_thread_init(None)
#lv2_lib.lv2_threads_init(None)  # lv2
