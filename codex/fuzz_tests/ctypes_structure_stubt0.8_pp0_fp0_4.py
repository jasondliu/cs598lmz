import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_float

s = S(1, 1.0)
print s.x, s.y
</code>
It's excessive to use unions and structures only to extract a single field. I find it particularly hard to reason about the memory layout in that case; I strongly suggest you stick with numpy arrays.
If you really do need to manipulate memory directly, <code>ctypes</code> is a much better choice than <code>struct</code>.

