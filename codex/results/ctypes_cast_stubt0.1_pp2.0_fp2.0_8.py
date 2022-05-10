import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes.cast()函数将一个整数转换为指针，然后再转换回整数，这个整数和原来的整数是相等的。
# 但是，如果我们将这个整数当作指针使用，就会得到一个错误。
# 因为这个整数并不指向任何内存空间，所以访问它会导致一个段错误。

# ctypes.cast(0, ctypes.py_object).value
# Segmentation fault (core dumped
