import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __init__(self, *args, **kwargs):
        print "CField.__init__", args, kwargs
        super(CField, self).__init__(*args, **kwargs)

ctypes.CField = CField

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

print S.x

# output:
# CField.__init__ ('x', <class 'ctypes.c_int'>) {}
# <Field type=c_int, ofs=0, size=4>
