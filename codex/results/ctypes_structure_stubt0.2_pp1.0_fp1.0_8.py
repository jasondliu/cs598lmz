import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
print s.x
print s.y
</code>
The output is:
<code>0
0
</code>
I would expect the output to be:
<code>0
Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    print s.y
AttributeError: 'S' object has no attribute 'y'
</code>
Why is the second attribute <code>y</code> not defined?


A:

The <code>_fields_</code> attribute is a list of 2-tuples, each of which is a field name and a field type.  The field name is a string, not a variable name.  So, the <code>_fields_</code> attribute should be:
<code>_fields_ = [('x', ctypes.c_int), ('y', ctypes.
