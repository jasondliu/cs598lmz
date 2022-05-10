import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f(x):
    x.x = 5

s = S()
print s.x
f(s)
print s.x
</code>
prints
<code>0
5
</code>
If you want a copy, use <code>copy.deepcopy</code>.

