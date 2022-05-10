import ctypes
import ctypes.util
import threading
import sqlite3
import os.path

from . import sanei
from . import dll


# TODO: implement into settings
debug = False
# debug = True

# libsane needs these values to establish a connection
connect_flags = dll.SANE_MUST_RELOAD
# connect_flags = (
#     dll.SANE_MUST_RELOAD
#     | dll.SANE_UNIX_LOW_LEVEL_API
#     | dll.SANE_TEST_SETTINGS_INVALID
# )

sane_globals = None
sane_device_s = None
sane_scanner_s = None
sane_int_async_t = None
sane_parameters_s = None
sane_params_t = None
sane_device_t = None
sane_scanner_t = None
sane_option_type_t = None

lock = threading.Lock()


