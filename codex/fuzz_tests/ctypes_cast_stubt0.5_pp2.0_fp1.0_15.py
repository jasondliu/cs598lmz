import ctypes
ctypes.cast(some_pointer, ctypes.py_object).value

# 使用ctypes模块的指针类型
# ctypes.POINTER(ctypes.c_int)
# 定义一个结构体
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

# 结构体实例
p = Point(11, y=22)
# 打印坐标值
print('({}, {})'.format(p.x, p.y))
# 获取x坐标值
print(p.x)
# 获取y坐标值
print(p.y)

# 定义一个结构体数组
class Line(ctypes.Structure):
    _
