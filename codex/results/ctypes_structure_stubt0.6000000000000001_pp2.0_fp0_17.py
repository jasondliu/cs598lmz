import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

s = S()
s.x = 5
print(s.x)
</code>
If I run this code, I get this error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: can't set attribute
</code>
What am I doing wrong?


A:

You need to change <code>x</code> to <code>_x</code> (double underscore) to make it an actual attribute.

