import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong
    z = ctypes.c_longlong
    w = ctypes.c_longlong

print(ctypes.sizeof(S))
print(ctypes.alignment(S))

s = S()
print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
print(ctypes.addressof(s.y))
print(ctypes.addressof(s.z))
print(ctypes.addressof(s.w))
</code>
Output:
<code>$ python3 test.py
32
8
140267848753952
140267848753952
140267848753960
140267848753968
140267848753976
</code>

