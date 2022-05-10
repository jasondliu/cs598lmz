import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes模块中的Structure类型可以定义一个结构化的数据类型。
# 它可以让你定义C语言中的struct类型。

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

p = Point(11, y=22)
p.x, p.y

# 可以使用ctypes中的POINTER类型创建指针。
# 下面演示了如何创建一个指向上面定义的Point类型的指针。


