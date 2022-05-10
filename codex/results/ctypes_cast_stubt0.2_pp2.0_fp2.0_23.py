import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 2

import os
import sys
import time
import warnings
import weakref
import threading
import traceback
import ctypes
import ctypes.util
import _ctypes
import _multiprocessing
from _multiprocessing import win32, get_errno, timeout_default
from _multiprocessing import RECURSIVE_MUTEX, RECURSIVE_MUTEX_INCREMENT
from _multiprocessing import SEMAPHORE, SEMAPHORE_INCREMENT
from _multiprocessing import Lock, RLock, Condition, Semaphore, BoundedSemaphore
from _multiprocessing import Value, Array, RawValue, RawArray
from _multiprocessing import current_process, active_children
from _multiprocessing import cpu_count
from _multiprocessing import Connection, Pipe, PipeConnection
from _multiprocessing import reduction
from _multiprocessing import ForkingPickler
from _multiprocessing import Connection, Pipe
