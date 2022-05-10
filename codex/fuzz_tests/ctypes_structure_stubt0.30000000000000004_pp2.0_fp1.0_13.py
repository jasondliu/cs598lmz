import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

# ctypes.Structure is a subclass of ctypes.Union
assert issubclass(ctypes.Structure, ctypes.Union)

# ctypes.Union is a subclass of ctypes.Structure
assert issubclass(ctypes.Union, ctypes.Structure)

# ctypes.Structure is a subclass of ctypes.Union
assert isinstance(s, ctypes.Union)

# ctypes.Union is a subclass of ctypes.Structure
assert isinstance(s, ctypes.Structure)
</code>
I'm not sure if this is a bug or a feature.

