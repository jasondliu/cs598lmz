import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()

foo = S()
foo.x = -2
foo.x.value = -3
print(foo.x)
assert foo.x == -3
</code>
which prints
<code>-3
</code>

