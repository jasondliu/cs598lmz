import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works fine. But if I try to return a list, it fails:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1,2,3]

print(fun())
</code>
This gives the error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    print(fun())
SystemError: &lt;built-in function fun&gt; returned a result with an error set
</code>
I'm using Python 3.7.4 on Windows 10.
How can I return a list from a C function?


A:

The problem is that <code>ctypes</code> is trying to convert the list to a <code>PyObject*</code> pointer, but it's not a pointer.
You can use <code>ctypes.pythonapi.PyList_New</code> to create a new list object, and
