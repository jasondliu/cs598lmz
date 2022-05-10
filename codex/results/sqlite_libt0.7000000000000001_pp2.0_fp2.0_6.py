import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import time
import re
import os
import platform

from .utils import *
from .winutils import *

import logging
log = logging.getLogger("dbg")

# flag for enabling/disabling the attempt to fix memory faults that occur during the debuggee's exception handler
# Set the value to False for debugging
FIX_EXCEPTION_CHAIN = True

# flag indicating whether to use an alternate exception handler that works around a bug in PyDbgEng
USE_SAFE_EXCEPTION_HANDLER = False

# prevents cyclic references between objects that would otherwise prevent garbage collection
# this is a generic debug object that can be used to hold a reference to any object the user might
# need a global reference to
class DebugObject(object):
    pass

# PyDbgEng instance
g_dbg = None

# global reference object
g_obj = DebugObject()

# global dbgeng callback objects
g_dbgeng_callbacks = None

g_dbgeng_completion = None

# global event callback objects
g_dbg_call
