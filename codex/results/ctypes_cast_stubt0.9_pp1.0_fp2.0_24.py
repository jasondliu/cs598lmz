import ctypes
ctypes.cast(id(my_int), ctypes.py_object).value

my_int = int('420')
hex(id(my_int))
ctypes.cast(id(my_int), ctypes.py_object).value

# 这个例子中，相当于维护了一个引用计数为零的对象，如果一个对象的引用计数为零，就会被收回，通常会在下一次垃圾回收阶段
# 还原，因此那么就有机会在其检查新的引用计数时为之增添一个引用，就如
