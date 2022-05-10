import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

    def __repr__(self):
        return 'S(%s, %s)' % (self.x, self.y)

s = S()
s.x = 1
s.y = 2
print(s)

s2 = s
s2.x = 3
print(s)
</code>
I would expect the output to be
<code>S(1, 2)
S(3, 2)
</code>
But instead I get
<code>S(1, 2)
S(3, 2)
</code>
I would have expected <code>s2</code> to be a copy of <code>s</code>, but it seems that it is actually a reference, as changing <code>s2</code> also changes <code>s</code>.
I'm using Python 3.4.1 on Windows 7.


A:

You need to use the <code>from_address()</code> method to create a new object from the same memory location:
<code>s2
