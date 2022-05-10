import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

# 可以使用from_buffer函数创建一个结构体类型对象，它将一个字节序列解释为一个结构体。
# 下面的代码使用from_buffer创建了一个结构体对象，然后使用结构体的x和y字段访问字节序列的前8个字节。

import ctypes

