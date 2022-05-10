import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print s.x
print s.y
</code>
This code prints:
<code>0
0
</code>
Is there a way to get the following output?
<code>1
1
</code>
I am looking for a way to initialize the structure members with a value other than 0.


A:

You can use <code>__init__</code> for that:
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    def __init__(self):
        ctypes.Structure.__init__(self)
        self.x = 1
        self.y = 1

s = S()
print s.x
print s.y
</code>

