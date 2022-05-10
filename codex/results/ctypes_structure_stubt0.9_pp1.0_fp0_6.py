import ctypes

class S(ctypes.Structure):
    x = 42

x = S()
ctypes.addressof(x.x)
</code>
Output:
<code>Traceback (most recent call last):
  File "&lt;input&gt;", line 5, in &lt;module&gt;
IndexError: tuple index out of range
</code>
I am developing a low-level C-library (C wrapper) for developers, so I just want to be sure I am not missing something.
Edit: I know doing this is a bad idea in production code, but that is not my concern here. Also, the reason ctypes is mentioned here is a simplified example using its API.


A:

If you really need to look at the memory layout of a <code>ctypes.Structure</code>, but don't have the C source code that declared it, you can use the <code>offset</code> property of a member description.
<code>In [1]: import ctypes

In [2]: class S(ctypes.Structure):
   ...:     _pack_ = 1
   ...:     _fields_ = [("x", ctypes
