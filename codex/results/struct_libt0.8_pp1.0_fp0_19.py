import _struct
import _thread
import _threading
import time
import unittest
from test import support

# Skip this test if the thread module isn't there.
threading = support.import_module('threading')
thread = support.import_module('thread')
_thread = support.import_module('_thread')
# Skip this test if _thread is None
threading = threading and _thread
thread = thread and _thread
_thread = _thread and _thread

# Usually, threads run concurrently.  In this case, we want to force
# serial execution for some tests, to avoid a race condition.
# We use a counter for that.
concurrency = 3
concurrency_counter = 0
concurrency_counter_lock = _threading.Lock()
def serialize_using_counter(n=1):
    global concurrency_counter
    global concurrency_counter_lock
    concurrency_counter_lock.acquire()
    concurrency_counter += 1
    n = n - 1
    while n > 0:
        n = n - 1
        concurrency_counter += 1
       
