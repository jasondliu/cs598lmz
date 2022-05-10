import gc, weakref
from collections import defaultdict
from concurrent.futures._base import PENDING
from concurrent.futures.thread import (
    BrokenThreadPool,
    _WorkItem,
    ThreadPoolExecutor,
)


class BrokenThreadPool2(ThreadPoolExecutor):
    _broken = True

    def _adjust_thread_count(self):
        pass

    def shutdown(self, wait=True):
        pass


