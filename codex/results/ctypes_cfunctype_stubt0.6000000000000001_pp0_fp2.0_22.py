import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello")
    return "hello"

fun()
</code>
The above code works fine.
But when I try to return a list or an array, it gives me an error.
<code>import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello")
    return [1,2,3]

# return np.array([1,2,3])

fun()
</code>
I get the following error:
<code>TypeError: can't return value with type 'list'
</code>
What is the correct way to return a list or an array?


A:

You can return a <code>ctypes.py_object</code> object that contains the list or array.
<code>import ctypes
import numpy as np

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello")
    return ctypes.py_object([1
