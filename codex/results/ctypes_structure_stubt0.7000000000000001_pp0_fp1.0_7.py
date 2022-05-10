import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("x", ctypes.c_int)]

print(S.x)
</code>
output:
<code>1
</code>

