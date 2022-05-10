import ctypes

class S(ctypes.Structure):
    x = 10

s = S()
print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
</code>
Output:
<code>4481966416
4481966416
</code>

