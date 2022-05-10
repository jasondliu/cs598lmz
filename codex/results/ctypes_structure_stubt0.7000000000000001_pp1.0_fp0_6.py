import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    pass

s = S()

s.x = 10

print(s.x)
</code>
Output:
<code>0
</code>
Why is <code>x</code> not <code>10</code>?


A:

Because <code>x</code> is a class attribute, not an instance attribute, so it's shared by all instances of <code>S</code>, and you haven't set it yet.
You would have to use <code>__init__</code> to create an instance attribute:
<code>class S(ctypes.Structure):
    def __init__(self):
        self.x = ctypes.c_int()

s = S()
s.x = 10
print(s.x)
</code>

<code>10
</code>

