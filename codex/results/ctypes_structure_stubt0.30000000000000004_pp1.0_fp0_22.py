import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x)
print(s.y)
print(s.z)

print(s.__dict__)

print(s.__sizeof__())

print(S.__dict__)

print(S.__sizeof__())

print(S.__name__)

print(S.__module__)

print(S.__doc__)

print(S.__bases__)

print(S.__dictoffset__)

print(S.__flags__)

print(S.__itemsize__)

print(S.__basicsize__)

print(S.__str__)

print(S.__repr__)

print(S.__hash__)

print(S.__call__)

print(S.__getattribute__)

print(
