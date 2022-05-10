import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    def __init__(self):
        self.x = 1
        self.y = 2

s = S()
print s.x
print s.y
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "./test.py", line 12, in &lt;module&gt;
    s = S()
TypeError: __init__() takes exactly 1 argument (2 given)
</code>
I am using Python 2.6.5.
What am I doing wrong?


A:

I think you need to use the <code>_fields_</code> attribute to define your structure members:
<code>class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    def __init__(self):
        self.x = 1
        self.y = 2
</code>

