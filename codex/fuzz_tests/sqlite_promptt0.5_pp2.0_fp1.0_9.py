import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import sqlite3

def test_thread_local():
    """
    This test is a bit complicated.  First we need to find the
    address of the current thread state.  The address is unique,
    and we can use it as a key in a dictionary.  If we can get
    the same object back out of the dictionary, then it works.
    """
    # First, get the address of the thread state.
    thread_state = ctypes.c_long()
    PyThreadState_Get = ctypes.pythonapi.PyThreadState_Get
    PyThreadState_Get.restype = ctypes.POINTER(ctypes.c_long)
    PyThreadState_Get.argtypes = [ctypes.POINTER(ctypes.c_long)]
    PyThreadState_Get(ctypes.byref(thread_state))

    # Now, create a dictionary keyed by thread state address.
    thread_state_dict = {}

    # Store the current thread state in the dictionary.
    thread_state_dict[thread_state.value] = ctypes
