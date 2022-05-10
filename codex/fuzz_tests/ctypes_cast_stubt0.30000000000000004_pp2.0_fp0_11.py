import ctypes
ctypes.cast(1, ctypes.py_object)

# 创建一个类型
class POINTER(ctypes.c_void_p):
    pass

ctypes.cast(1, POINTER)

# 创建一个类型
class POINTER(ctypes.c_void_p):
    _type_ = "P"

ctypes.cast(1, POINTER)

# 创建一个类型
class POINTER(ctypes.c_void_p):
    _type_ = "P"

    def _sub_addr_(self):
        return self.value + 1

ctypes.cast(1, POINTER)

# 创建一个类型
class POINTER(ctypes.c_void_p):
    _type_ = "P"

    def _sub_addr_(self):
        return self.value + 1

    def _sub_addr_size_(self):
        return c
