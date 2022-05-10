import types
types.MethodType(lambda self: None, None)

# classes
class A(object):
    def __init__(self):
        pass

class B(A):
    def __init__(self):
        A.__init__(self)

# multiple inheritance
class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

# import
import sys

# from ... import
from types import MethodType

# try/except/finally
try:
    pass
except:
    pass
finally:
    pass

# with
with open('filename') as f:
    pass

# raise
raise ValueError
raise ValueError("message")
raise ValueError("message") from None

# assert
assert False
assert False, "message"

# del
del var

# global
global_var = 0
def f():
    global global_var
    global_var = 1

# nonlocal
def outer():
    x = "old"
    def inner
