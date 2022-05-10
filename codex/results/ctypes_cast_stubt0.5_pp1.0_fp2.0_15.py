import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes库的POINTER方法创建指针类型
ctypes.POINTER(ctypes.c_int)

# 使用ctypes库的pointer方法创建指针
p = ctypes.pointer(ctypes.c_int(42))
p.contents

# 利用ctypes库提供的Structure类创建结构体
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

# 利用ctypes库提供的Union类创建联合
class ShortPoint(ctypes.Union):
    _fields_ = [('x', ctypes.c_short),
                ('y', ctypes.c_short)]
