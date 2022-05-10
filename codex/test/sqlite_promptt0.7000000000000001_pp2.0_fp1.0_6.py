import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import logging
logging.basicConfig(level=logging.DEBUG)

import sqlitedict


class IterationError(ValueError):
    pass

class IterationTimeout(IterationError):
    pass

def _check_iteration(container, timeout=0.05):
    threads = threading.enumerate()
    if len(threads) == 1:
        # Only the main thread is running
        return

    def check_threads():
        threads = threading.enumerate()
        if len(threads) > 1:
            raise IterationError("Iteration blocked by %s" % (threads[1], ))

    if timeout is not None:
        t = threading.Timer(timeout, check_threads)
        t.start()
    try:
        for x in container:
            pass
    except IterationError:
        raise
    except Exception:
        raise IterationError("Iteration failed")
    finally:
        if timeout is not None:
            t.cancel()


