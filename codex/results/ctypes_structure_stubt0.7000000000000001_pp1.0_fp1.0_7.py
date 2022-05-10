import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_float()

s = S()

s.x = 3.0
s.y = 4.0

print s.x, s.y
</code>
It defines a structure and creates an instance of the structure, then assigns values to the x and y members of the structure.
But it crashes on the line that assigns a value to s.x with a segmentation fault. Why?


A:

I think the problem is that you are trying to access the members of the S class directly. The way to access them is as attributes of an instance of the class. Try this:
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float), ("y", ctypes.c_float)]

s = S()
s.x = 3.0
s.y = 4.0
print s.x, s.y
</code>

