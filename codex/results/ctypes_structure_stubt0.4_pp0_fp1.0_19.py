import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 42
s.y = 17

print(s.x)
print(s.y)

s2 = S(1, 2)
print(s2.x)
print(s2.y)

# 可以通过访问_fields_来获得结构体的成员名
print(s._fields_)

# 可以通过访问_fields_来获得结构体的成员名
print(s._fields_)

# 可以通过访问_fields_来获得结构体的成员名
print(s._fields_)

# 可以通过访问_fields_来获得
