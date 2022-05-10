import ctypes
ctypes.cast(ctypes.pointer(c_int(0x12345678)), ctypes.POINTER(ctypes.c_char))[:4]

# 输出十六进制字符串
print(ctypes.cast(ctypes.pointer(c_int(0x12345678)), ctypes.POINTER(ctypes.c_char))[:4].hex())
