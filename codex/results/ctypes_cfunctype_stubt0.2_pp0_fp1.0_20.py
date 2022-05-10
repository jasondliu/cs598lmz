import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>
The error is:
<code>TypeError: 'CFUNCTYPE' object is not callable
</code>
I have also tried:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun.__call__()
</code>
The error is:
<code>TypeError: 'CFUNCTYPE' object is not callable
</code>
I have also tried:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun.__call__(fun)
</code>
The error is:
<code>TypeError: 'CFUNCTYPE' object is not callable
</code>
I have also tried:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE

