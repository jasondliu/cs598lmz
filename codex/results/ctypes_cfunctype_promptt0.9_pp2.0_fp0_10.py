import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)()
print ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)()
print ctypes.FunctionType(None, None)

from _ctypes import CThunkObject, CDLL
from _ctypes import PyObj_FromPtr
class MyCThunk(CThunkObject):
    def __init__(self, whatevs, *args):
        CThunkObject.__init__(self, whatevs, *args)
        print 'MyCThunk init: ', whatevs, args
    def __call__(self):
        print('my cthunk call')
        return super(MyCThunk, self).__call__()

ctypes.PyDLL.__bases__ = MyCThunk, CDLL

# Hack on CThunk_dealloc. Inject our own CThunk class.
#
MyCThunk_dealloc = ctypes._memmove_addr
#print ctypes._memmove_addr, id(ctypes._mem
