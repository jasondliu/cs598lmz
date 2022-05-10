import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(S.x.offset)
print(S.x.size)
</code>
The output is <code>0</code> and <code>4</code> respectively.
If you're using Python 3.3 or later, you'll need to use <code>int.bit_length()</code> instead of <code>int.__sizeof__()</code>.

