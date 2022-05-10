import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)

import os
import sys
import time
import threading
import traceback
import types
import weakref

from . import _multiprocessing
from . import connection
from . import util
from . import context
from . import process
from . import PipeConnection
from . import reduction
from . import semaphore_tracker
from . import win32
from . import win32_support
from . import ForkAwareThreadLock
from . import get_logger

#
#
#

logger = get_logger()

#
#
#

#
# Constants representing the state of a process
#

RUN = 0
CLOSE = 1
TERMINATE = 2

#
#
#

class AuthenticationError(Exception):
    pass

#
#
#

class BufferTooShort(Exception):
    pass

#
#
#

class Process(object):

    '''
    Class which supports the process object of multiprocessing.
    '''

   
