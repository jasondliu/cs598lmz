import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# 可以看到，int 是一个 class，而非 type
# 所以，你可以把它的实例赋值给某个变量，然后，后面的代码就可以判断变量是否是该类型
# 而对于一个 type，它的实例就是类，所以，你无法从 type 的实例中判断这个类是否是该 type

# 通过 type()函数判断的是一个对象是否是函数
# 通过types
