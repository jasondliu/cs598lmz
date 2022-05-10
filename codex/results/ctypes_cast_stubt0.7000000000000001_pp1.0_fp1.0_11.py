import ctypes
ctypes.cast(p, ctypes.py_object).value

# 4. 直接调用函数指针
# 如果指针指向的是一个C函数，可以直接在python中调用。
# 这个操作需要使用ctypes模块。
import ctypes
libc = ctypes.CDLL('libc.so.6')
libc.printf('Hello World')

# 5. 使用指针的底层内存
# 读取一个字符串的末尾并获取其地址。
s = 'Hello World'
p = ctypes.pointer(ctypes.c_char.from_buffer(s))
p[-1]
p.address

# 6. 使用
