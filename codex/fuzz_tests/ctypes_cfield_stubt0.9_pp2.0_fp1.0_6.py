import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
class A(object):
    pass

def dump(obj, file=None):
    pickle.dump(obj, file)

#ctypes.CField.__module__ = 'ctypes'
#dump(ctypes.CField, open('p3.pk', 'wb'))

pickle.load(open('p3.pk', 'rb'))
