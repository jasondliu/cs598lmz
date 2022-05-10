import ctypes
ctypes.cast(0x7ffff7dd26d0, ctypes.py_object).value

# 0x7ffff7dd26d0  内存地址
# ctypes.py_object  类型 内存地址
# .value 属性

# 也就是说，这句话的作用是把0x7ffff7dd26d0这个内存地址，以py_object类型转换，然后获取这个地址中的value属性

# 实际上，ctypes.cast(0x7ffff7dd26d0, ctypes.py_object) 就是把0x7ffff7dd26d0这个内存地址，转换为py_object类
