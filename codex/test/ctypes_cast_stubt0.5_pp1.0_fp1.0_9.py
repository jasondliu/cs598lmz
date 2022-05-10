import ctypes
ctypes.cast(ctypes.pointer(ctypes.c_int(3)), ctypes.c_void_p)

# ==> c_void_p(3)

# 如果没有可用的类型，还可以使用 ctypes.c_char_p 和 ctypes.c_wchar_p 类来表示 C 的 char* 和 wchar_t* 类型，但是这种情况下，可能需要自己将数据复制到可以被 C 库使用的内存缓冲区中。
#
# 另一个可能的方案是使用 ctypes.create_string_buffer() 函数来构建一个可变的字符
