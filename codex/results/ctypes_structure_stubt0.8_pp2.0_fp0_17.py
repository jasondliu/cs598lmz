import ctypes

class S(ctypes.Structure):
    x = x = ctypes.c_int
    y = y = ctypes.c_float

s = S(10, 20)
print(s.x)
print(s.y)
</code>
Receiving the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    s = S(10, 20)
  File "/usr/lib/python3.6/ctypes/__init__.py", line 364, in __init__
    self._b_base_ = self._b_needsaddr_ = byref(self)
TypeError: a bytes-like object is required, not 'int'
</code>
Why is this happening?


A:

You are not initializing the class correctly, because the <code>x</code> and <code>y</code> fields of your <code>S</code> class are NOT  the same as your variables <code>x</code> and <code>y</code>. In fact, they are actually functions of the <code>ctypes
