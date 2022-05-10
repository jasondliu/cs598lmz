import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:", check_same_thread=False)

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

# Test libc.pthread_self()

# Test libc.pthread_mutex_init()

# Test libc.pthread_mutex_lock()

# Test libc.pthread_mutex_unlock()

# Test libc.pthread_mutex_destroy()

# Test libc.pthread_mutex_t
pthread_mutex_t = ctypes.c_int

# Test libc.pthread_mutexattr_t
pthread_mutexattr_t = ctypes.c_int

def pthread_mutexattr_default():
    return pthread_mutexattr_t()

def pthread_mutex_default():
    return pthread_mutex_t()

class pthread_mutex_wrapper(object):
    """
    A wrapper for pthread_mutex_t
    """
