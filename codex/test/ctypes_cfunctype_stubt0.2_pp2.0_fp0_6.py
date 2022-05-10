import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()

# ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
# ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
# ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object)
# ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object)
# ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object)
# ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py
