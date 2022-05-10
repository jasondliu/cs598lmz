import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 3
s.y = 4
print s.x, s.y
</code>
The output is:
<code>3 4
</code>
But if I define the class as:
<code>class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    def __init__(self):
        self.x = 3
        self.y = 4

s = S()
print s.x, s.y
</code>
Then the output is:
<code>0 0
</code>
What is the problem?


A:

The problem is that you are defining an <code>__init__</code> method that doesn't call the base <code>Structure</code> <code>__init__</code> method. You need to call it, like this:
<code>class S(ctypes.Structure):
    _fields_ = [
        ('x',
