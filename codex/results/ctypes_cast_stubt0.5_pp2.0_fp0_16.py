import ctypes
ctypes.cast(0x12345678, ctypes.c_float)

# result:
# c_float(305419896.0)

# 以上代码将整数转换为浮点数，将整数的低位字节看作浮点数的符号、指数和尾数部分。

# 从某种程度上来讲，ctypes是一个内存视图（memory view）工具。
# 它可以通过特定的数据类型去解释一块二进制数据，从而实现各种不同的转换操作。

#
