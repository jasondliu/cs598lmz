import ctypes
ctypes.cast(ctypes.c_char_p(b'Hello, world!'), ctypes.POINTER(ctypes.c_int))

# 为了从指针指向的内存中获取数据，可以使用 ctypes 内建的内存访问函数
# 比如，要将给定的整数值转换为字符串，可以这样做：
import ctypes

def make_array(n):
    return (n * ctypes.py_object)()

# 创建一个长度为 10 的数组，并且将每个元素初始化为 None
arr = make_array(10)
