import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()
print s.x
print s.y

s.x = 3
s.y = 4
print s.x
print s.y
</code>
When I run this, I get the following output:
<code>$ python s.py
1
2
3
4
</code>
However, when I change the structure to have an <code>__init__</code> method, like this:
<code>class S(ctypes.Structure):
    def __init__(self):
        self.x = ctypes.c_int(1)
        self.y = ctypes.c_int(2)

s = S()
print s.x
print s.y

s.x = 3
s.y = 4
print s.x
print s.y
</code>
I get the following output:
<code>$ python s.py
1
2
1
2
</code>
Why do the assignments to <code>
