import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

s = S()

def f():
    return ctypes.addressof(s)

print f()
print f()
</code>
Sample output:
<code>3224104
3224104
</code>
The address is the same each time.

