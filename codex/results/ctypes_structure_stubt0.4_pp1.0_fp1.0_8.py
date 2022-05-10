import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    y = ctypes.c_int(1)

s = S()

print s.x
print s.y

s.x = 42

print s.x
print s.y
</code>
This outputs:
<code>0
1
42
1
</code>
As you can see, the <code>x</code> field gets set to 42, but <code>y</code> remains 1. 
How can I make it so that when I create an instance of <code>S</code>, the fields are initialized to the values specified in the class definition?


A:

You can use <code>__init__</code>:
<code>class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

    def __init__(self):
        self.x = 0
        self.y = 1
</code>

