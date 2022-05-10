import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# This should not modify s.x:
def modify_int():
    s = S()
    s.x = 42
    # This should be optimized to mem[int, void *] = void *
    ctypes.CFuncPtr.from_address(id)(ctypes.c_voidp)
    print s.x

modify_int()
