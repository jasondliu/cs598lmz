import ctypes
ctypes.cast(c_int(0), ctypes.py_object).value

# 使用ctypes.cast()将c_int对象转换为py_object对象，然后再调用其value属性，
# 就可以获取到这个对象的值了。

# ctypes.cast()函数的第一个参数是要转换的对象，第二个参数是转换后的类型。
# 这个函数返回一个新的对象，它的值和原对象相同，但类型不同。

# ctypes.cast()函数的
