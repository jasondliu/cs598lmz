import ctypes
# Test ctypes.CField

# This test is a failure case.

# When first called, it stores a pointer to a function as a Python
# function (`foo`).  This pointer is cast to an integer and stored in a
# CField.  This is then converted back to a Python function.  Because
# the CField is a Python function, it is treated as a new function and
# gets its own refcount, so when it is deleted, the refcount for the
# original `foo` is reduced by one.  This means that the refcount for
# `foo` is 1 before the first call and 0 after the second call.  The
# code must not allow the second call to happen, because it tries to
# call a deleted function.

class CF2(ctypes.Structure):
    _fields_ = [("f", ctypes.CFunctionType(ctypes.c_int, []))]

def f():
    return 5

def g():
    a = CF2()
    a.f = f
    f.__name__ = 'foo'
    a2 = CF2.from_address(ctypes
