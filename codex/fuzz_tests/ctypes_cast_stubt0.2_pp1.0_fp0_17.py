import ctypes
ctypes.cast(id(self), ctypes.py_object).value

# 在Python中，每个对象都有一个__dict__属性，它是一个字典，用来存储对象的变量。
# 如果你有一个实例a，那么a.__dict__就是一个字典，它包含了a的所有成员变量。
# 如果你有一个类A，那么A.__dict__也是一个字典，它包含了A的所有成员函数。
# 如果你有一个模块m，那么m.__dict
