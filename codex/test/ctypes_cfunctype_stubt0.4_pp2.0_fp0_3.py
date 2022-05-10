import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

# ctypes.cast(obj, typ)
# ctypes.cast(obj, ctypes.c_int)
# ctypes.cast(obj, ctypes.py_object)
# ctypes.cast(obj, ctypes.py_object).value

# ctypes.POINTER(ctypes.c_int)
# ctypes.POINTER(ctypes.py_object)
# ctypes.POINTER(ctypes.py_object).from_address(id(obj))
# ctypes.POINTER(ctypes.py_object).from_address(id(obj)).contents

# ctypes.cast(obj, ctypes.POINTER(ctypes.py_object)).contents
# ctypes.cast(obj, ctypes.POINTER(ctypes.py_object)).contents.value

# ctypes.cast(obj, ctypes.POINTER(ctypes.py_object)).contents.value = 123
# ctypes.cast(obj, ctypes.POINTER(ctypes.py_object)).contents = 123
# ctypes.cast
