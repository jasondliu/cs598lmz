import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.s = S()
        self.s.x = 1

c = C()

# Python 3.4.0a2 (default:4af4cc4d7c4d, Sep  6 2013, 15:38:07) [MSC v.1600 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import test_ctypes
# >>> c = test_ctypes.C()
# >>> c.s.x
# 1
# >>> c.s.x = 2
# >>> c.s.x
# 2
# >>> c.s.x = 3.0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: must be an integer, not float
# >>> c.s.x = 'abc'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError
