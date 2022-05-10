import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    def __repr__(self):
        return "S(%s)" % self.x

s = S()
print s
s.x = 42
print s
</code>
Here is the output:
<code>S(0)
S(42)
</code>

