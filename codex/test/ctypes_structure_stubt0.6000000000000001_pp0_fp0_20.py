import ctypes

class S(ctypes.Structure):
    x = 1

s = S()
print(s.x)

s.x = 2
print(s.x)

try:
    s.x = 'hello'
except TypeError as e:
    print('Error: ' + str(e))

s.x = 3
print(s.x)

s.x = 4.0
print(s.x)

s.x = None
print(s.x)

s.x = [1, 2, 3]
print(s.x)

s.x = (1, 2, 3)
print(s.x)


class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

s2 = S2()
print(s2.x)

s2.x = 2
print(s2.x)

try:
    s2.x = 'hello'
except TypeError as e:
    print('Error: ' + str(e))

s2.x = 3
print(s2.x)

