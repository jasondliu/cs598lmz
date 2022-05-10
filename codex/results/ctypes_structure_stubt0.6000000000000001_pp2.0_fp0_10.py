import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2
print s.x, s.y
</code>
This is the output:
<code>1 0
</code>
Why is <code>s.y</code> equal to 0? Is this the right way to define structures?
Thank you.


A:

The initializers for <code>ctypes.Structure</code> attributes are called after the instance is created.  So in your case, both <code>x</code> and <code>y</code> are initialized to <code>0</code>, then <code>x</code> is assigned <code>1</code>.
You can define your own <code>__init__</code> method to fix that:
<code>class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    def __init__(self, x=0, y=0):
        self.x
