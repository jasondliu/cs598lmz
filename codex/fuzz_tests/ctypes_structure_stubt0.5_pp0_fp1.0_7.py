import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
s.x = 1
print(s.x)

# 这里我们会看到一个错误
# s.x = 'abc'

# 不过可以用下面的方法处理
s.x = ctypes.c_int('abc')
print(s.x)

# 或者
s.x = ctypes.c_int.from_parameter('abc')
print(s.x)

# 但是这个方法只能处理基本数据类型
# 对于字符串的处理

s.x = ctypes.c_char_p('abc')
print(s.x)

# 如果是一个数组的话
s.x = (ctypes.c_char *
