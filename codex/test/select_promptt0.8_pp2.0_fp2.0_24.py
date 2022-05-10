import select
# Test select.select() on a socket pair.
import threading
from test.test_support import run_unittest, reap_children
import Queue
import errno
from select import error as SelectError

class InterruptableThread(threading.Thread):
    def run(self):
        while True:
            v = self.queue.get()
            if v is None:
                break
            elif v == "exception":
                raise Exception('Thread exception')
            elif v == "timeout":
                raise self.queue.Empty
            elif v == "blocking":
                self.queue.put(v)
                break
            elif v == 'raiseKeyboardInterrupt':
                # Raise our own KeyboardInterrupt to ensure that
                # it is masked in the interrupted thread.
                raise KeyboardInterrupt
