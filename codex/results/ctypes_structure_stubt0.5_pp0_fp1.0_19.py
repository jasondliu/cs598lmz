import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)

s = S()
s.x = 1.0

print s.x
</code>
I get the error:
<code>Traceback (most recent call last):
  File "./test.py", line 9, in &lt;module&gt;
    s.x = 1.0
TypeError: can't set attributes of built-in/extension type 'S'
</code>
I can't seem to find any documentation about this.
I'm using Python 2.7.3 on Ubuntu 12.04.


A:

I think you're looking for the <code>c_double</code> class, not the <code>c_double</code> type.
<code>class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double)]

s = S()
s.x = 1.0

print s.x
</code>

