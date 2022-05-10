import ctypes
ctypes.cast(0, ctypes.py_object).value

# 利用ctypes模块创建指针
i = ctypes.c_int(42)
p = ctypes.pointer(i)
print(p)

# 指针操作
p.contents
p.contents.value
p.contents.value = 0
p.contents.value

# 对象的内存地址
i = 10
id(i)

# 指针到普通对象的转换
p = ctypes.pointer(ctypes.c_int(42))
p.contents
p.contents.value
p.contents.value = 0
p.contents.value

# 复制对象
s = [1, 2, 3]
t = s
t[1] = 4
print(s)

# 对象的
