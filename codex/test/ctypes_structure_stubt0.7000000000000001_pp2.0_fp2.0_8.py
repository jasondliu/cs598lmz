import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float

s = S()
print(type(s.x), s.x)
print(type(s.y), s.y)

# &lt;class 'int'&gt; 0
# &lt;class 'float'&gt; 0.0
