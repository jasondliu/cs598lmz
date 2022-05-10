import ctypes
ctypes.cast(ctypes.c_int(100), ctypes.c_double)

# 1.3.4 字节字符串上的字符串操作
data = b'Hello World'
data[0:5]
data.startswith(b'Hello')
data.split()
data.replace(b'Hello', b'Hello Cruel')

# 1.3.6 对象引用、可变性以及垃圾回收
# 变量赋值的本质是引用
# 可变对象：list、dict、bytearray、user-defined classes
# 不可变对象：string、tuple、bytes
# 在函数中修改可变对象的值，对本地变量是可见
