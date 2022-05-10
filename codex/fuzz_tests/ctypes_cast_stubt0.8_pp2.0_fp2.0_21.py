import ctypes
ctypes.cast(h, ctypes.c_void_p)

c_int_p = ctypes.POINTER(ctypes.c_int)
ctypes.cast(h, c_int_p)

ctypes.cast(h, ctypes.c_char_p).value
ctypes.cast(h, ctypes.c_void_p).value
ctypes.cast(h, c_int_p).contents

ctypes.cast(h, ctypes.c_char_p).value = b'012345'
ctypes.cast(h, ctypes.c_void_p).value = 0
ctypes.cast(h, c_int_p).contents.value = b'012345'

# 6.7 函数返回值在ctypes中的处理
# 6.7.1 基本的返回类型
# 6.7.2 数组类型
# 6.7.3 函数指
