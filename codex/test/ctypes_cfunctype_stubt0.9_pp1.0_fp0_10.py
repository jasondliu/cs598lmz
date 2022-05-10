import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 7

class A(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return '<A %r>' % (self.x,)

