import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

class C(object):
    def __init__(self, fun):
        self.fun = FUNTYPE(fun)

def f(x):
    return x**2

c = C(f)
print c.fun(2)
</code>
However, if I pass a function to the <code>C</code> constructor which depends on nonlocal variables, I get an error:
<code>def f(x):
    a = 1
    return a*x

c = C(f)
</code>
Traceback:
<code>Traceback (most recent call last):
  File "test.py", line 15, in &lt;module&gt;
    c = C(f)
  File "test.py", line 8, in __init__
    self.fun = FUNTYPE(fun)
  File "/usr/lib/python2.7/ctypes/__init__.py", line 354, in __init__
    self._flags_ = _flags_
  File "/usr/lib
