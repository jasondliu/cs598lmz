import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong
    z = ctypes.c_longlong
    w = ctypes.c_longlong

t = S()
print type(t)
print type(t.x)
print t.x
print t.x.value
print t.x.value == 0

t.x.value = 1
print t.x.value == 1
print t.x == 1
print t.x == 1
print t.x.value == 1

print t.x.value == 1
t.x = 2
print t.x == 2
print t.x.value == 2

print t.x.value == 2
t.x.value = 3
print t.x.value == 3
print t.x == 3
