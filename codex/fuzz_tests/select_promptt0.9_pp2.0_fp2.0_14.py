import select
# Test select.select with Timeout
from multiprocessing.util import Finalize
from multiprocessing import Process, RLock
from weakref import WeakValueDictionary
import multiprocessing.util
from test.fork_wait import ForkWait
from test.support import run_unittest, int_from_bytes, requires_IEEE_754
from test.support.threading_helper import threading_setup
import time
import ctypes
import gc
from pydebug import debug


class _TestFinalize(object):
    # This can be used to test the atexit freeing of resources
    started = False
    finished = False

    def __init__(self):
        self.pid = os.getpid()
        self.tid = threading.get_ident()
        assert self.tid != _main_thread

        # If a manager is created in the main thread then __exit__ doesn't
        # delete the weakref because __del__ doesn't get called when the
        # process exits.
        _after_fork_registry.clear()

    def __enter__(self):

