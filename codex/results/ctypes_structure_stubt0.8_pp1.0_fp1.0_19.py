import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

c = ctypes.c_int.from_address(id(S))
print(c)

# Create a new S instance
s = ctypes.py_object.from_address(ctypes.addressof(c))
print(s)

print(s.x)
print(s.y)

# Modify the instance
s.x = 1
s.y = 2
print(s.x)
print(s.y)

# Create a new instance
s2 = ctypes.py_object.from_address(ctypes.addressof(c))
print(s2.x)
print(s2.y)
</code>
The code above outputs:
<code>c_long(1)
&lt;class '__main__.S'&gt;
0
0
1
2
1
2
</code>

