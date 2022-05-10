import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() and .execute()

import time

# Declare the global variables
libc = ctypes.CDLL(ctypes.util.find_library('c'))

__all__ = [ 'O_RDONLY', 'O_WRONLY', 'O_RDWR', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC',
            'O_CREAT', 'O_DIRECT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_LARGEFILE',
            'O_NOATIME', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_NDELAY', 'O_SYNC',
            'O_TRUNC', 'O_TTY_INIT', 'O_PATH',
            'S_ISUID', 'S_ISGID', 'S_ENFMT', 'S_ISVTX', 'S_IREAD', 'S_IWRITE',
            'S_IEXEC', 'S_IRWXU', '
