import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
print fun()
</code>
The output is:
<code>hello
</code>
If I change the code to:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
print fun()
print fun()
</code>
The output is:
<code>hello
hello
</code>
However, if I change the code to:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
print fun()
print fun()
print fun()
</code>
The output is:
<code>hello
hello
hello
hello
</code>
If I change the code to:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
print fun()
print fun()
print fun()
print fun
