import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
fun()

# class MyFunType(ctypes.CFUNCTYPE):
#     _restype_ = ctypes.py_object
#     _argtypes_ = []
# @MyFunType
# def fun():
#     return 42
# fun()

# @ctypes.CFUNCTYPE(ctypes.py_object)
# def fun():
#     return 42
# fun()

# @ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
# def fun(arg):
#     return arg
# fun(42)

# @ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
# def fun(arg):
#     return arg
# fun(42)

# @ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
# def fun(arg):
#     return arg
# fun(42)

# @ctypes.CFUNCTYPE(ctypes.py_object,
