import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()

print s.x, s.y
</code>
This prints out <code>1 2</code>.  The <code>x</code> and <code>y</code> members are <code>c_int</code> instances, not just integers.  You can access the integer values using the <code>value</code> attribute:
<code>print s.x.value, s.y.value
</code>

