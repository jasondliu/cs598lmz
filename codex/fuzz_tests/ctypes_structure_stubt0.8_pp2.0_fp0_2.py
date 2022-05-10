import ctypes

class S(ctypes.Structure):
    x = 1
    y = x + 1
    z = x + 2
    w = y + z
    _fields_ = [("a", ctypes.c_int, y),
                ("b", ctypes.c_int, z),
                ("c", ctypes.c_int, w),
                ("d", ctypes.c_int, x)]

print(S.x, S.y, S.z, S.w)
print(S.d, S.a, S.b, S.c)
</code>
The output is:
<code>1 2 4 7
3 1 2 4
</code>
it's obvious that <code>S.d</code> is defined before <code>S.a</code>, but in the output <code>S.a</code> is defined before <code>S.d</code>.
I think this is due to bit field packing (the ending padding for <code>S.d</code> is not enough for the first 5 bits). But how come the ending padding for <code>S.b</code> is ok?


A:
