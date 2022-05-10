import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 42
s.y = 43
print s.x, s.y
print S.x, S.y
print s.x.value, s.y.value
print S.x.value, S.y.value
</code>
This outputs
<code>42 43
42 43
42 43
0 0
</code>
If you want to access the class attribute, you need to use <code>S.x</code> and <code>S.y</code> (or <code>S.x.value</code> and <code>S.y.value</code>) instead of <code>s.x</code> and <code>s.y</code>.

