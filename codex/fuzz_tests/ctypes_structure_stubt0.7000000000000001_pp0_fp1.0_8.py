import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 4
    _fields_ = [('x', x)]

S.x.offset = 4
print S.x.offset
print ctypes.sizeof(S.x)
</code>
This code is from https://docs.python.org/3/library/ctypes.html#structures-and-unions.
But I get the error:
<code>Traceback (most recent call last):
  File "ex6.py", line 4, in &lt;module&gt;
    S.x.offset = 4
AttributeError: attribute 'offset' of 'CField' objects is not writable
</code>
So I am wondering if this is a problem with my Python version, or something else. The current version of Python I am using is 2.7.12.

