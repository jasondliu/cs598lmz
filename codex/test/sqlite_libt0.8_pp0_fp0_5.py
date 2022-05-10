import ctypes
import ctypes.util
import threading
import sqlite3
import time
import ssl
import re
import struct

from ._queue import _Queue
import _rbtree as rbt
import heapq as _heapq

from . import _queue
from ._dummy_thread import exit

import _queue

#
# A bit of information about the threading implementation:
#
# Thread objects are stored in dictionaries that map ident to thread
# objects. Ident is a unique integer allocated by _newident()
# function.
#
# The ident dictionaries are actually weak dictionaries: when a thread
# exits and there are no remaining references to it as a local variable
# in some stack frame, the ident dictionary entry for it disappears.
#
# However, simply deleting the ident dictionary entry doesn't mean
# the thread object is lost: there may be references to it that are
# contained in traceback objects (such as sys.exc_info()[2]), which
# are not weak references.  To collect these objects, we use a temporary
# list of all thread objects, since Python doesn't provide any way to
# enumerate all the objects of a given type. The list
