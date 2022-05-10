import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes模块的POINTER()函数，可以创建指针类型。
# 下面是一个简单的例子，它定义了一个c_int类型的指针，然后把一个c_int变量的地址赋给这个指针：
import ctypes
i = ctypes.c_int(42)
pi = ctypes.pointer(i)
print(pi)
print(pi.contents)

# 指针的contents属性是一个对象，它包含指针指向地址的原始值。

