import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_long
    def __init__(self):
        self.x = 7.0
        self.y = 3

a = S()
print a.x, a.y
</code>
I get the error:
<code>RuntimeError: maximum recursion depth exceeded
</code>
If I make <code>x=tests.c_double(7.0)</code>, then I get a <code>MemoryError</code>.
I've tried changing around the order of x,y and initializing x,y with different types and I always get the same errors.


A:

You didn't create the type <code>S</code>; you just defined it.  To create a type, you need to call <code>type</code>:
<code>S = type('S', (ctypes.Structure,), dict(x=ctypes.c_double, y=ctypes.c_long))
</code>
Now you can create an instance of <code>S</code>:
<code>&gt;&gt;&gt
