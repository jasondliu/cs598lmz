import ctypes
ctypes.cast(id(0), ctypes.py_object).value

# 可以看到，id(0)被转换成了一个ctypes.py_object类型的对象，
# 并且获取到了它的value属性，这个属性就是Python对象的内存地址。

# 将这个内存地址转换成一个整数，就可以用来表示这个对象的唯一标识符了。

# 在Python中，每个对象都有一个唯一的标识符，这个标识符
