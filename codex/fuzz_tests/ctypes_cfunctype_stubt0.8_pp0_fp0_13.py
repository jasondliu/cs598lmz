import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
</code>
For the details of the call, see the CPython source code: the <code>call_function</code> opcode first reads the function object (<code>fun</code> in the example), then the argument tuple (<code>()</code> in the example), before calling the function.
So you can see that the function object cannot have any argument. It only has a return type.
Your function <code>fun</code> defined a pointer to a function with a <code>ctypes.py_object</code> return type (a Python object).
To create functions with multiple arguments, you need to pass a tuple of ctypes objects representing the argument types, as shown in the ctypes doc. For example:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(arg1, arg2):
    return 42
</code>
This creates a pointer to a function taking two Python objects as arguments.

