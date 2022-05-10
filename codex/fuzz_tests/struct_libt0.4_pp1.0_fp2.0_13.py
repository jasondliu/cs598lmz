import _struct
import sys
import threading
import time

import numpy as np

from . import lib
from . import numpy_support
from . import util

class _AsyncResult(object):
    def __init__(self, req):
        self.req = req
        self.event = threading.Event()
        self.status = None
        self.exception = None

    def wait(self):
        self.event.wait()
        if self.exception is not None:
            raise self.exception

    def get(self):
        self.wait()
        return self.status


class _AsyncContext(object):
    def __init__(self):
        self.queue = collections.deque()
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()

    def _run(self):
        while True:
            req = self.queue.popleft()
            status = req.wait()
            req.status = status
            req.event.set()

   
