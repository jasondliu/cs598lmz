import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
s.x = 1
print(s.x)

# 这里我们会看到一个错误
# s.x = 'abc'

# 不过可以用下面的方法处理
