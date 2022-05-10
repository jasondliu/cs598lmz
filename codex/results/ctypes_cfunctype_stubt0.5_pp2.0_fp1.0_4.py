import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def f():
    return fun()

f()
</code>
This fails with:
<code>Traceback (most recent call last):
  File "C:\Users\mike.boers\Desktop\foo.py", line 7, in &lt;module&gt;
    f()
  File "C:\Users\mike.boers\Desktop\foo.py", line 5, in f
    return fun()
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
I'm not sure what I'm doing wrong.


A:

The problem is that the <code>__call__</code> method of <code>ctypes.CFUNCTYPE</code> objects is implemented in C, which means it doesn't use the <code>__call__</code> method of the <code>ctypes.py_object</code> object that is returned.  Instead it calls <code>PyObject_Call</code> directly.  This means that it doesn't have access to the <code>__call__
