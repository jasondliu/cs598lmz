import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y
</code>
This works fine, but I'd like to be able to access the members of the structure by name.  I tried to do this by adding the following line to the end:
<code>print s.x, s.y, s.x + s.y
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    print s.x, s.y, s.x + s.y
AttributeError: 'S' object has no attribute 'x'
</code>
I tried to add the following to the structure definition:
<code>S._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
</code>
But I get the same error.  I also tried to add the following:
<code>S._fields
