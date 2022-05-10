import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5
</code>
Can I somehow convert the <code>FUNTYPE</code>-type object <code>fun</code> to Python callable object?


A:

Just in case you need to pass <code>fun</code> to a function that takes a python callable and expect the function to be called like any other python callable, you can use <code>ctypes.pythonapi.PyCFunction_Call</code>:
<code>import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5

ctypes.pythonapi.PyCFunction_Call(ctypes.py_object(fun), ctypes.c_void_p(), ctypes.py_object())
</code>

