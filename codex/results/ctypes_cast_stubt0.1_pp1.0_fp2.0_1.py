import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes.cast()将一个整数转换成一个指针，然后使用.value属性访问指针指向的内存
# 但是这种方式有个缺陷，就是它不能访问到真实的内存，只能访问到虚拟内存
# 因为Python的虚拟内存管理器会把所有的内存都映射到一个连续的地址空间中，
# 而ctypes.cast()只能访问到这
