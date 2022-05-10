import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

from . import _sqlite3
from . import util
from . import _util

# Cache for the sqlite3.connect() function.
_connect_cache = {}

# Cache for the sqlite3.Connection.create_function() method.
_create_function_cache = {}

# Cache for the sqlite3.Connection.create_aggregate() method.
_create_aggregate_cache = {}

# Cache for the sqlite3.Connection.create_collation() method.
_create_collation_cache = {}

# Cache for the sqlite3.Connection.set_authorizer() method.
_set_authorizer_cache = {}

# Cache for the sqlite3.Connection.set_progress_handler() method.
_set_progress_handler_cache = {}

# Cache for the sqlite3.Connection.set_trace_callback() method.
_set_trace_callback_cache = {}

# Cache for the sqlite3.Connection.set_update_hook() method.
_set
