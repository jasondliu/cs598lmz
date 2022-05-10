import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

def f(x):
    return S(x, 2)

print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))
</code>
Output:
<code>(1, 2)
(2, 2)
(3, 2)
(4, 2)
(5, 2)
</code>

