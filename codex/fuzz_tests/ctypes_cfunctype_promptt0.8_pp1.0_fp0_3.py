import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_int and ctypes.c_int32, as well as
# POINTER(c_int)
if ctypes.sizeof(ctypes.c_int) == 4:
    c_int32 = ctypes.c_int
else:
    c_int32 = ctypes.c_int32

import operator

iscfunction = types.isbuiltin if PY2 else types.isfunction
iscmethod = types.ismethod if PY2 else types.ismethoddescriptor

class CmpContextManager(object):
    def __init__(self, op):
        self._op = op
    def __enter__(self):
        self._old_op = operator.gt
        operator.gt = self._op
        return self._old_op
    def __exit__(self, tp, v, tb):
        operator.gt = self._old_op

class CFunction(ctypes.c_void_p):
    """Use to create a ctypes prototype for a C function.
    """
    def __new__(self
