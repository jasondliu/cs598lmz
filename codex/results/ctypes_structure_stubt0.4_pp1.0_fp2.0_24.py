import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

s = S()
print s.x
print s.y
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:\Users\David\Desktop\test.py", line 11, in &lt;module&gt;
    print s.y
AttributeError: 'S' object has no attribute 'y'
</code>
Why is this?


A:

It's because you're assigning to <code>x</code> before the <code>_fields_</code> attribute is set.  The <code>_fields_</code> attribute is used to generate the class attributes, so this is the same as doing:
<code>s = S()
s.x = 1
print s.x
print s.y
</code>

