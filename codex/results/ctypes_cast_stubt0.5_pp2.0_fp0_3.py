import ctypes
ctypes.cast(ptr, ctypes.py_object).value

# 使用这个方法可以得到指针的地址
id(ptr)

# 如果要从地址中获取指针，则使用如下方法：
ptr = ctypes.cast(id(x), ctypes.POINTER(ctypes.c_int))

# 如果要将一个可变类型转换为指针，则需要使用byref()函数
a = ctypes.c_int(42)
a_ptr = ctypes.byref(a)
print(a_ptr)
# <ctypes.c_long object at 0x1099b9c30>

a_ptr.contents
# c_long(42)
