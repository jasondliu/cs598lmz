import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s.__dict__)
print(s.__dict__.keys())
print(s.__dict__.values())
</code>
Output:
<code>1
2
{}
dict_keys([])
dict_values([])
</code>

