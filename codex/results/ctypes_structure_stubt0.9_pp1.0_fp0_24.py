import ctypes

class S(ctypes.Structure):
    x = ctypes.Structure()
    _fields_ = [('x', "")]

class S2(ctypes.Structure):
    _fields_ = [('x', "")]
S2.x = S2

class S3(ctypes.Structure):
    _fields_ = [('x', "")]
S3.x = 1
</code>
Outputs:
<code>Traceback (most recent call last):
  File "&lt;input&gt;", line 1, in &lt;module&gt;
TypeError: expected a structure, a pointer or an array
Traceback (most recent call last):
  File "&lt;input&gt;", line 1, in &lt;module&gt;
TypeError: incorrect type specification
Traceback (most recent call last):
  File "&lt;input&gt;", line 3, in &lt;module&gt;
TypeError: incorrect type specification
Traceback (most recent call last):
  File "&lt;input&gt;", line 3, in &lt;module&gt;

