import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
print(fun())
</code>
The output is
<code>42
</code>

You can get the address of a Python function with <code>id()</code>.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return 42
print(id(fun))
</code>
The output is
<code>140562225443744
</code>

You can use <code>ctypes.CFUNCTYPE</code> to create a function pointer that takes a function pointer as its argument.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(arg):
    return arg()
@FUNTYPE
def fun2():
    return 42
print(fun(fun2))
</code>
The output is
<code>42
</code>

You can call a function pointer that takes a function pointer as its argument.
<code>import ctypes
FUNTYPE = ctypes.
