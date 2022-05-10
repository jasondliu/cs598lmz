import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import sys
import os
import re
import time
import socket
import struct
import select
import errno
import traceback
import threading
import logging
import weakref
import collections
import platform

# SOURCE LINE 18

try:
    import ssl
except ImportError:
    ssl = None

# SOURCE LINE 23

try:
    import resource
except ImportError:
    resource = None

# SOURCE LINE 28

try:
    import fcntl
except ImportError:
    fcntl = None

# SOURCE LINE 33

try:
    import _thread
except ImportError:
    _thread = None

# SOURCE LINE 38

try:
    import _dummy_thread as dummy_thread
except ImportError:
    try:
        import dummy_thread
    except ImportError:
        dummy_thread = None

# SOURCE LINE 47

try:
    import msvcrt
except ImportError:
    msvcrt = None
