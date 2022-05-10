import select
# Test select.select() with readable and writable objects.
import errno
import os
import unittest
import socket
import collections
import fcntl
import time
import sys
try:
    import threading
except ImportError:
    threading = None
try:
    import resource
except ImportError:
    resource = None
try:
    import syslog
except ImportError:
    syslog = None
try:
    import fcntl
except ImportError:
    fcntl = None


from test import support
if not hasattr(support, 'get_attribute'):
    def get_attribute(obj, name):
        return getattr(obj, name)
else:
    get_attribute = support.get_attribute
try:
    set
except NameError:
    from sets import Set as set


def wait_for_io(func, args=(), timeout=30.0):


    def consume(q):
        try:
            while 1:
                q.get_nowait()
        except Empty:
            return
    q = Queue()
