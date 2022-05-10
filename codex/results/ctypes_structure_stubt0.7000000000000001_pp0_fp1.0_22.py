import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short
    z = ctypes.c_short

class C(ctypes.Structure):
    _fields_ = [("s0", S), ("s1", S)]

c_instance = C()

c_instance.s0.x = 1
c_instance.s0.y = 2
c_instance.s0.z = 3

c_instance.s1.x = 4
c_instance.s1.y = 5
c_instance.s1.z = 6

print(c_instance.s0.x)
print(c_instance.s0.y)
print(c_instance.s0.z)

print(c_instance.s1.x)
print(c_instance.s1.y)
print(c_instance.s1.z)

s = S()
s.x = 1
s.y = 2
s.z = 3
print(s.x)
print(s.y)
print(s.z)

print(
