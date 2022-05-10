import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os


def load_library(name):
    """Load a native library.

    This is a convenience method to load the library with ctypes.
    The function tries to load the library with the following
    name patterns:

    - ``{name}.so``
    - ``lib{name}.so``
    - ``lib{name}.dylib``
    - ``{name}.dylib``
    - ``{name}.dll``

    The function returns ``None`` if the library could not be loaded.

    :param name: The name of the library to load.
    :return: The loaded library or ``None`` if the library could not be loaded.
    """
    lib_path = ctypes.util.find_library(name)
    if lib_path is None:
        return None
    return ctypes.CDLL(lib_path)


def set_thread_name(name):
    """Set the name of the current thread.

    This function uses the ``pthread_setname_np`` function on platforms that
    support it.

    :param name: The name of the thread
