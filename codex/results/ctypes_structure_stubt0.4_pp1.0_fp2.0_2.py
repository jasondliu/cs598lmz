import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int)
    ]

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x)
print(s.y)
print(s.z)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    s.x = 1
  File "/usr/lib/python2.7/ctypes/__init__.py", line 353, in __setattr__
    self._set(fieldname, value)
  File "/usr/lib/python2.7/ctypes/__init__.py", line 358, in _set
    self._set_field(fieldname, value)
  File "/usr
