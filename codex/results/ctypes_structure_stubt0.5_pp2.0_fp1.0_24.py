import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

s = S()
print(s.x)
s.x = 1
print(s.x)
print(S.x.__doc__)
</code>
Output:
<code>0
1
x
</code>

