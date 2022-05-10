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


class ThreadPoolExecutorTest(unittest.TestCase):
    def test_submit(self):
        pool = ThreadPoolExecutor(1)
        done_event = threading.Event()

        def done():
            done_event.set()

        try:
            with self.assertRaises(RuntimeError) as cm:
                pool.submit(lambda: done())
                pool.submit(lambda: done())
            self.assertEqual(str(cm.exception), "cannot schedule new futures after shutdown")
        finally:
            pool.shutdown()

        self.assertTrue(done_event.is_set())

        with brokenThreadPool2
