import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    name = ctypes.c_char * 4

print(S.__dict__)
s = S()
print(s.__dict__)
s.x = 1
s.y = 2
s.name = b'abc'
print(s.x, s.y, s.name)
