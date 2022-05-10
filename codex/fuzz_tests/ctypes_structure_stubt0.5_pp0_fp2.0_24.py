import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Structure):
    x = S
    y = S

s = S()
t = T()

t.x.x = 1
t.x.y = 2
t.y.x = 3
t.y.y = 4

print(t.x.x)
print(t.x.y)
print(t.y.x)
print(t.y.y)
</code>
Output:
<code>1
2
3
4
</code>

