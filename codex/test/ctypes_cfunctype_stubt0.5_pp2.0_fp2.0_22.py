import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

# Create a new instance of the PythonInterpreter class.
# This will automatically call Py_Initialize()
