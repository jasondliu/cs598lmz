import ctypes
ctypes.cast(0, ctypes.py_object).value

# TypeError: NULL pointer access
# 因为python的指针不能指向空，也不能指向非法内存区域

# ctypes.POINTER() 创建指针类型
# ctypes.pointer(obj) 创建一个指向obj对象的指针
# POINTER(c_int) 表示c_int类型的指针
# POINTER(POINTER(c_int)) 表示c_int类型的指针的指针

i = c_int(42)
p = pointer(i)
assert p.contents.value == 42

# 让指针指向另一
