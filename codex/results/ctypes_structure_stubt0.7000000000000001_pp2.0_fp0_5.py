import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    z = ctypes.c_int(3)

s = S()
print(s.x, s.y, s.z)
s.x = 5
print(s.x, s.y, s.z)

# this is not allowed
# s.x = 3.2

try:
    s.x = 'x'
except TypeError as e:
    print(e)

# this is allowed, but the result is not meaningful
s.x = '5'
print(s.x)
print(type(s.x))
print(s.x.value)
print(type(s.x.value))

print('-'*20)

class S2(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)
    ]
# this is not allowed
# s2 = S2(x='x')

s2 = S2
