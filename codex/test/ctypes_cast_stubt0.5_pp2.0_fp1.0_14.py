import ctypes
ctypes.cast(ctypes.c_void_p(0x1f6a4), ctypes.c_void_p).value

# 你可以使用ctypes来访问内存中的结构体。 例如，假设你想访问一个C语言结构体：

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT(10, 20)
print(p.x)

# 这里有一个更复杂的例子，它演示了如何使用 ctypes 和一个共享库来访问系统函数库。

# 假设
