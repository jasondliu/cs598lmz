import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()
print(s.x)
print(s.y)
print(s.x._objects)
print(s.x._objects.keys())
print(s.x._objects.values())
print(s.x._objects.items())
print(s.x._objects.get('x'))
print(s.x._objects.get('y'))

class S_Nested(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    sub = S()

s_nested = S_Nested()
print(s_nested.x)
print(s_nested.y)
print(s_nested.sub.x)
print(s_nested.sub.y)
print(s_nested.sub.x._objects)
print(s_nested.sub.x._objects.keys())
print(s_nested.sub.x
