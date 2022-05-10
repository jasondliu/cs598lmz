import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class A(object):

    def __init__(self):
        self.f = fun

a = A()
print a.f
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "./test_ctypes.py", line 13, in &lt;module&gt;
    a = A()
  File "./test_ctypes.py", line 8, in __init__
    self.f = fun
TypeError: cannot be converted to a buffer.
</code>
I have <code>ctypes</code> version 1.1.0 in Python 2.7.
What am I doing wrong?


A:

<code>class A(object):

    def __init__(self):
        self.f = fun
</code>
should be
<code>class A(object):

    def __init__(self):
        self.f = fun()
</code>
<code>fun</code> is a function, <code>fun()</code> is the result of calling <code
