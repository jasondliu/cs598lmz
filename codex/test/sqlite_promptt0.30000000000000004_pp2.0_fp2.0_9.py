import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import numpy as np

import pytest

from pysat import sqlite3_db
from pysat.examples.test_instruments import TestInstrument
from pysat.examples.test_methods import TestLoad

libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Create a new shared memory block.
# This has size 1 byte.
shmid = libc.shmget(ctypes.c_int(0x12345), ctypes.c_int(1),
                    ctypes.c_int(0o666 | 0o1000000))
if shmid == -1:
    raise Exception("Failed to create shared memory block")

# Attach the shared memory block so that we can read/write to it.
shm = ctypes.c_void_p(libc.shmat(ctypes.c_int(shmid), ctypes.c_void_p(),
                                 ctypes.c_int(0)))

