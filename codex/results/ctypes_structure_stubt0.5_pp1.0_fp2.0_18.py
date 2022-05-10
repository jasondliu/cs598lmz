import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.in_dll(ctypes, "x")
    y = ctypes.c_int.in_dll(ctypes, "y")
    z = ctypes.c_int.in_dll(ctypes, "z")

print S.x, S.y, S.z

S.x.value = 10
S.y.value = 20
S.z.value = 30

print S.x, S.y, S.z
</code>
Output:
<code>0 0 0
10 20 30
</code>

