import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1/0
fun()

#assert_raises(ZeroDivisionError, fun)
#assert_raises(TypeError, ctypes.CFUNCTYPE(fun))
#assert_raises(TypeError, ctypes.CFUNCTYPE(None))
#assert_raises(TypeError, ctypes.CFUNCTYPE([]))
#assert_raises(TypeError, ctypes.CFUNCTYPE(1))

#def func(x):
#    print(x)
#    return x

#assert_raises(TypeError, ctypes.CFUNCTYPE(1, func))
#assert_raises(TypeError, ctypes.CFUNCTYPE(1.0, func))
#assert_raises(TypeError, ctypes.CFUNCTYPE([], func))
#assert_raises(TypeError, ctypes.CFUNCTYPE((), func))
#assert_raises(ValueError, ctypes.CFUNCTYPE((1,), func))
#assert_raises(ValueError, c
