import ctypes
# Test ctypes.CFUNCTYPE()
class Array:
    def __init__(self, data):
        self.data = []
        self.data = data
    def get_element_at(self, index):
        return self.data[index]

array = Array([1.5, 2.5])

# CFUNCTYPE是用来定义函数指针的类型，包括WIN32 DLL和callback
# 当定义函数指针新函数原型时，必须给出返回类型以及参数类型。
# 这些参数必须是ctypes能识别的类型，比如c_int, c_void_p, c_char_p等
# 另一种方
