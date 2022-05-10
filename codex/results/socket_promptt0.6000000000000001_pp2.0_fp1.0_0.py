import socket
# Test socket.if_indextoname
assert socket.if_indextoname(1) == "lo"
assert socket.if_indextoname(2) is None

import array
# Test array.typecodes
assert "bBhHiIlLqQfd" == "".join(sorted(array.typecodes))

import time
# Test time.tzname
assert time.tzname == ('UTC', 'UTC')

import _thread
# Test _thread.stack_size
assert _thread.stack_size() > 0

# Test getattr
class A:
    def __init__(self):
        self.x = 1
    def f(self):
        pass
a = A()
assert getattr(a, "x") == 1
assert getattr(a, "y", 2) == 2
assert getattr(a, "f") == a.f

# Test getattr on builtins
import builtins
assert getattr(builtins, "abs") == abs

# Test getattr on modules
import sys
assert getattr(sys, "path") == sys.path

# Test get
