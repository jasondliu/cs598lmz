import ctypes
ctypes.c_int32.from_address(ctypes.addressof(obj.x))

# 如果你想构建一个能够被指定为 C 函数参数的类型，你需要使用 ctypes.POINTER() 来构建指针类型
ctypes.POINTER(ctypes.c_int32)

# 为了构造指向某种类型的指针，你可以像下面这样使用 from_address() 方法：
p = ctypes.pointer(ctypes.c_int32(42))
p.from_address(id(obj.x))

# 如果你想操作内存中的
