import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        del delays[:]

signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)
signal.signal(signal.SIGALRM, handler)

while delays:
    pass

# -*- coding: utf-8 -*-
# https://docs.python.org/3.6/library/signal.html
import functools, signal

def timeout(seconds, error_message=""):
    def decorated(func):
        result = ""

        def _handle_timeout(signum, frame):
            nonlocal result
            result = error_message
            raise TimeoutError(error_message)
        
        def wrapper(*args, **kwargs):
            nonlocal result
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
                return result

        return functools.wraps(func)(wrapper)
    return
