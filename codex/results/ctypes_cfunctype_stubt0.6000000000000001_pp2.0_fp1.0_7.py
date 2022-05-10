import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

print fun()
</code>
It prints <code>0</code>.
On the other hand, if I change <code>0</code> to <code>False</code>, it gives the error:
<code>$ python test.py
Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    print fun()
  File "/usr/lib/python2.7/dist-packages/ctypes/__init__.py", line 366, in __call__
    return self.func(*args)
TypeError: 'PyCObject' object is not callable
</code>
I guess the problem is <code>None</code>, <code>False</code> and <code>0</code> are all equal to <code>False</code> in Python, but they are not equal to each other.
Is there a way to return <code>False</code> in a C function?


A:

I'm not sure why it doesn't work, but I think you can use <code>None</code> instead of
