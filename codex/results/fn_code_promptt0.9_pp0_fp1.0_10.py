fn = lambda: None
# Test fn.__code__ behavior
import re
# For testing module, global and builtin namespaces
import math
# For testing __import__() builtin
import struct
# For testing __import__() builtin
import imp
# For testing __import__() builtin
import types
# For testing __import__() builtin
import sys
# For testing __import__() builtin
import unittest

import threading
import traceback
# ------------------------------------------------------------------- code object
# Create a global variable x (defines __globals__ dict)
x = 2

# Create a function object f
def f(): pass

# Test __new__
CodeType = type(f.__code__)
assert CodeType.__new__ is CodeType

# Test basic code attribute access
# This is using the CPython api, but that's ok
assert f.__code__.co_argcount == 0
assert f.__code__.co_filename == __file__
assert f.__code__.co_name == "f"
assert f.__code__.co_firstlineno == 10
assert isinstance(f.__code
