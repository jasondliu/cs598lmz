import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 100

# import ctypes
# loadobj = ctypes.CDLL('ObjWindow', mode=ctypes.RTLD_GLOBAL)
# def fun():
#     return 100
#
# result = loadobj.PyObject_CallFunction(fun, None)
# print(result)
