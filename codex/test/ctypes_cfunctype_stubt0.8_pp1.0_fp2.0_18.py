import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return {'This is': 'a dict'}
class Pointer(ctypes.Structure):
    _fields_ = [('pointerValue', ctypes.c_void_p)]
class Callback(ctypes.Structure):
    _fields_ = [
        ('funPtr', ctypes.c_void_p),
        ('env', ctypes.c_void_p),
        ('data', ctypes.c_void_p)
    ]
cb = Callback()
cb.funPtr = ctypes.cast(fun, ctypes.c_void_p).value
p = ctypes.pointer(cb)
pointer = Pointer()
pointer.pointerValue = ctypes.cast(p, ctypes.c_void_p).value

ptr = ctypes.c_void_p()
ptr.value = pointer.pointerValue

result = Callback.from_address(ptr.value)
