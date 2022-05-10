import ctypes
ctypes.cast(0, ctypes.py_object).value

# 这个报错是因为这个值是没有类型的，所以没有 value 属性
# AttributeError: _ctypes.PyCDataObject instance has no attribute 'value'

# 对于没有类型的值，可以用 from_address 方法，指定地址和类型
ctypes.cast(id(0), ctypes.py_object).value

# 查看某个对象的地址
id(0)
# 用 from_address 方法，指定地址和类型
ctypes.cast(id(0), ctypes.py_object).value

#
