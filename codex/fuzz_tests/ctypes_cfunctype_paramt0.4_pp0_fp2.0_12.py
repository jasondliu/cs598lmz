import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    return a+b

myfunc_c = FUNTYPE(myfunc)
print(myfunc_c(1, 2))

# ctypes.byref(obj)
# ctypes.byref() 可以将任何对象转换为 C 语言风格的指针。

# ctypes.POINTER(type)
# ctypes.POINTER() 可以创建指向某种类型对象的指针。

# ctypes.cast(obj, type)
# ctypes.cast() 可以将对象转换为另一种 ctypes 类型。

# ctypes.string_at(addr[, size])
# ctypes.
