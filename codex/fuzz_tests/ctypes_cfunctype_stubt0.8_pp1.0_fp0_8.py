import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return lambda x: 'hey there' + str(x)
</code>
In my case I'm using the function <code>py_object</code> as return type, but I can't find any way of changing the return value without changing the ctypes module itself, because the <code>_ctypes.py_object</code> only returns the <code>PyObject*</code> pointer and <code>py_object</code> function does not exist in <code>_ctypes</code>.
What I did was the following:
<code>import ctypes
import sys

def create_handlers(name, return_type, param_types):
    # Override the previous function.
    ctypes.pythonapi.PyObject_CallFunctionObjArgs.argtypes = param_types
    ctypes.pythonapi.PyObject_CallFunctionObjArgs.restype = return_type

    FUNTYPE = ctypes.CFUNCTYPE(return_type)
    return FUNTYPE((name, ctypes.pythonapi))

def create_function(name, return_type, param_types):
    def function(*
