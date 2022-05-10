import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

print S.__dict__['x'].offset
print S.__dict__['y'].offset
</code>
Output:
<code>0
4
</code>

