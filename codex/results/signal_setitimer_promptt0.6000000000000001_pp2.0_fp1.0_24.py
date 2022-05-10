import signal
# Test signal.setitimer()
import socket
# Test socket.gethostbyname()

# This is not imported, but it is used in a test.
class TestClass:
    pass

import sys

# Test sys.path

import threading
# Test threading.Thread()

import time
# Test time.strftime()

import traceback
# Test traceback.extract_stack()

# This is not imported, but it is used in a test.
class TestException(Exception):
    pass

import types
# Test types.FunctionType
# Test types.MethodType
# Test types.ModuleType

# This is not imported, but it is used in a test.
class TestUnicode:
    def __init__(self, value):
        self.value = value
    def __unicode__(self):
        return self.value
    def __str__(self):
        return str(self.value)
