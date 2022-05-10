import ctypes
# Test ctypes.CFUNCTYPE
def _callback(x, y):
    print(x, y)
    return x + y
    
CFuncType = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
c_func = CFuncType(_callback)
c_func(1, 2)

type(c_func)
 
class Struct_test(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]
                
struct_test = Struct_test(1, 2)

struct_test.x
struct_test.y
