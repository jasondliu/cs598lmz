import signal
# Test signal.setitimer
# See also: https://docs.python.org/3/library/itertools.html
# https://github.com/gkbrk/slowapi

import itertools

import resource
import time
import functools

TIMEOUT = 5


class TimeoutError(Exception):
    pass


def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return functools.wraps(func)(wrapper)

    return decorator


@timeout(TIMEOUT)
def slowfunc():
    print("slow function")
