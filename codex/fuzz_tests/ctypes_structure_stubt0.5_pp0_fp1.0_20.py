import ctypes

class S(ctypes.Structure):
    x =  ctypes.c_int
    y =  ctypes.c_int

s = S()
print(s.x)
print(s.y)
</code>
I get the following output:
<code>0
0
</code>
How can I create a new instance of S with values for x and y?  If I do:
<code>s = S(1,2)
</code>
I get the error:
<code>TypeError: __init__() takes exactly 1 argument (3 given)
</code>
What am I missing?


A:

You need to define an <code>__init__</code> method in your structure:
<code>class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

s = S(1,2)
print(s.x, s.y)
</code
