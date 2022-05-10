import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short
    z = ctypes.c_short
    w = ctypes.c_short

a = ctypes.c_int()
a = -1

s = S()
s.x = -1
s.y = -1
s.z = -1
s.w = -1

print a.value
print s.x, s.y, s.z, s.w
</code>
The output is:
<code>-1
-1 -1 -1 -1
</code>
So as you can see, <code>ctypes.c_int()</code> does not initialize the variable with 0, but with <code>0xffffffff</code>.
Now, if <code>ctypes.c_int</code> does not initialize a variable to 0, how do I do it?

Edit: I tried <code>ctypes.c_int(0)</code> which is documented to initialize with 0, but it doesn't, it still initializes with <code>0xffffffff</code>
