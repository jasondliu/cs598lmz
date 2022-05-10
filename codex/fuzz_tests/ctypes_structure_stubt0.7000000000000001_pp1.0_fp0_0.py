import ctypes

class S(ctypes.Structure):
    x = None

class D(S):
    pass

S.x = ctypes.c_int(42)

print D.x.value
</code>
Prints:
<code>42
</code>

