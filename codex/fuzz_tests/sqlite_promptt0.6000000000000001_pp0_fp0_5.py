import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memorydb?mode=memory&cache=shared')

import logging
logger = logging.getLogger(__name__)

import pysqlite2.dbapi2 as sqlite3

def _open(filename, flags, mode):
    return os.open(filename, flags, mode)

def _close(fd):
    return os.close(fd)

def _lock(fd, lock_type, whence, start, length):
    # lock_type = F_UNLCK, F_RDLCK, F_WRLCK
    whence = SEEK_SET if whence == sqlite3.SEEK_SET else SEEK_CUR
    return fcntl.lockf(fd, lock_type, length, start, whence)


# Use ctypes to access the BerkeleyDB functions.
#
# This is a bit of a hack, but it saves us from having to write a
# bunch of boilerplate C code and compile it.
#
# The BerkeleyDB functions we use are:
#
# db_create
# db_env_create
# db
