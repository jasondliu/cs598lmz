import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

def f():
    s = S()
    s.x = 1
    s.y = 2
    return s

print(f().x)
print(f().y)
</code>
This prints:
<code>1
2
</code>

