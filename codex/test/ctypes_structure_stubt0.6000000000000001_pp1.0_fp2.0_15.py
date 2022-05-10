import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
print(s.x)
s.x = 1
print(s.x)
s.y = 2
s.z = 3
print(s.x, s.y, s.z)

t = S()
t.x = 2
t.y = 3
t.z = 4

s = t
print(s.x, s.y, s.z)

print(type(s))
print(type(S))

# 列表转换为 ctypes 数组
l = [1, 2, 3]
sa = (ctypes.c_int * len(l))(*l)
print(sa)

# 字典转换为 ctypes 结构
d = {'x': 1, 'y': 2, 'z': 3}
sd = S(**d)
