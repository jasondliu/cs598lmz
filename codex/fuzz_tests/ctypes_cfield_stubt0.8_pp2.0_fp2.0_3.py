import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__module__ = 'ctypes'

# Hack required to prevent test_codecs getting confused by the old
# ctypes unittest.
if sys.modules.get('test.test_ctypes'):
    del sys.modules['test.test_ctypes']
del S
