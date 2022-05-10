import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16(1)
    y = ctypes.c_int16(2)

s = S()

print("%s" % s.x)
print("%s" % s.y)
print("%s" % (s.x + s.y))
</code>
This works fine. But if I try to do the same with a ctypes.Union, I get a TypeError:
<code>import ctypes

class U(ctypes.Union):
    x = ctypes.c_int16(1)
    y = ctypes.c_int16(2)

u = U()

print("%s" % u.x)
print("%s" % u.y)
print("%s" % (u.x + u.y))
</code>
The error message is:
<code>Traceback (most recent call last):
  File "./test.py", line 11, in &lt;module&gt;
    print("%s" % (u.x + u.y))
  File "/usr/
