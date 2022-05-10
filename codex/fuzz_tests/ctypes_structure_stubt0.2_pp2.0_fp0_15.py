import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

s = S()
print s.x
print s.y
</code>
The output is:
<code>0
0
</code>
I would expect the output to be:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    print s.x
AttributeError: 'S' object has no attribute 'x'
</code>
Why is the output not as expected?


A:

The <code>_fields_</code> attribute is used to create the <code>__slots__</code> attribute.  The <code>__slots__</code> attribute is used to create the <code>__dict__</code> attribute.  The <code>__dict__</code> attribute is used to store the attributes of the object.  So, <code>s.x</code> is stored in
