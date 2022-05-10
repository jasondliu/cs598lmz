import _struct
import sys
import time

from collections import deque
from itertools import izip
from multiprocessing import Process, Queue
from threading import Thread

try:
    from pydebugger.debug import debug
except ImportError:
    def debug(fn):
        return fn

try:
    from pydebugger.common import kill_self
except ImportError:
    def kill_self():
        os.kill(os.getpid(), signal.SIGKILL)

# TODO:
#   - get rid of "while True" loops

def _debug_log(msg):
    sys.stderr.write('%s\n' % msg)
    sys.stderr.flush()

def _debug_log_exception(msg):
    _debug_log('%s: %s' % (msg, sys.exc_info()[1]))

class _Thread(Thread):
    def __init__(self, name):
        super(_Thread, self).__init__()
        self.name = name

   
