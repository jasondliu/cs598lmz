import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import os
import sys
import time
import traceback
import threading
import atexit
import signal

# SOURCE LINE 12

try:
    import thread
except ImportError:
    import _thread as thread

# SOURCE LINE 16

try:
    import msvcrt
except ImportError:
    msvcrt = None

# SOURCE LINE 20

try:
    import _winapi
except ImportError:
    _winapi = None

# SOURCE LINE 24

try:
    import _multiprocessing
except ImportError:
    _multiprocessing = None

# SOURCE LINE 28

try:
    import _dummy_threading
except ImportError:
    _dummy_threading = None

# SOURCE LINE 32

try:
    import _threading_local
except ImportError:
    _threading_local = None

# SOURCE LINE 36

try:
    import _weakref
except ImportError:
   
