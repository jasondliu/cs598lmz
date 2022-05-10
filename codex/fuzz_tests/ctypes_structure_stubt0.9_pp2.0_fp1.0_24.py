import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 4

class S1(ctypes.Structure):
    _fields_ = [("x", S), ("y", ctypes.c_uint32)]


s = S1()
s.x = b"\x01\x02\x03"
s.y = 10
print("%s %s %s %s %s"% (s.x[0], s.x[1], s.x[2], s.x[3], s.y))
</code>
Output:
<code>1 2 3 0 10
</code>

