import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes模块操作内存
import ctypes

# 这里使用ctypes.c_char_p类型是因为这个类型可以自动转换为c语言字符串
# 如果使用ctypes.c_char类型的话，需要使用string_at()方法转换为字符串
# 如果使用ctypes.c_wchar_p类型的话，需要使用wstring_at()方法转换为字符串
# 如果使用ctypes.c_ubyte类型的
