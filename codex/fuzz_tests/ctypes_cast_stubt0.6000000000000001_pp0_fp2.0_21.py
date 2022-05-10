import ctypes
ctypes.cast(0, ctypes.py_object)

# 这个函数会返回一个指针，指向内存地址0，并且这个指针指向的类型为py_object
# 也就是说，这个指针指向的内存地址存储的是一个python对象
# 还有一个危险的地方就是ctypes还提供了一个POINTER类，可以像指针一样来操作它
# p = ctypes.POINTER(ctypes.py_object)
# p.contents = ctypes.py_object(42)
# print(p.contents.value)

