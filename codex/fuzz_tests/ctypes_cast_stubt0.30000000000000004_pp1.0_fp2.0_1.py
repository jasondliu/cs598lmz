import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes.cast()函数将整型转换为指针类型，然后再使用value属性获取指针指向的值。
# 但是，这种方法有个缺点，就是无法确定指针指向的是什么类型的变量，所以，需要一种更通用的方法。
# 在Python中，每个变量都有一个__class__属性，它指向变量所属的类。
# 比
