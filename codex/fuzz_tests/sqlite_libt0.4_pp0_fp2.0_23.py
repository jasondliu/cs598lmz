import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time
import struct
import os
import sys
import signal
import argparse

# from http://stackoverflow.com/questions/1191374/using-module-subprocess-with-timeout
class TimeoutException(Exception):
    pass

def timeout(seconds, error_message="Timeout"):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutException(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

class CmdTimeoutException(Exception):
    pass

class CmdTimeout(object):
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
