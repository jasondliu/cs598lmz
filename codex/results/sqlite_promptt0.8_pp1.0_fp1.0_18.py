import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# Store the callback function
g_callback = None

# Store the callback context
g_context = None


def valid_callback(callback, context):
    """Validate callback function."""
    if not callable(callback):
        raise ValueError('Invalid callback function')
    if context is None:
        context = threading.get_ident()
    return callback, context


def register_callback(callback, context=None):
    """Register a new callback."""
    global g_callback
    global g_context
    callback, context = valid_callback(callback, context)
    g_callback = callback
    g_context = context


def default_callback(context, event_type, arg1, arg2):
    """Default callback function."""
    print('{} {} {} {}'.format(context, event_type, arg1, arg2))


def test_callback(event_type, arg1, arg2):
    """Test callback function."""
    global g_callback
    global g_context
    if g_callback is None:
       
