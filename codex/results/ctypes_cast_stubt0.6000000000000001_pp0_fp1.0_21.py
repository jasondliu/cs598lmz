import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 使用这个方法需要注意的是，对于一些无法用这种方法访问的对象，有的会报错，有的会被截断，有的会显示不出来。
# 比如：
# 输出这个对象，只能显示一部分，缺<__main__.S object at 0x7f5d3b4c4cc0>
# 输出这个对象，会报错“TypeError: a bytes-like object is required, not 'str'”
# 输出这个对象
