import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
class A(object):
    def __init__(self):
        self.callable = fun

# This is how CPython works - callable() is called at the point where the
# class is defined, not at the point where it is actually called. So the
# default callable() will treat the fun() as a normal function, and that leads
# to the "NoneType is not callable" error.
a = A()
b = A()
a.callable()
</code>

