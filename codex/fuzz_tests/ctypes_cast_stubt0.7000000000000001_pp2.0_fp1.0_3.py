import ctypes
ctypes.cast(id(s), ctypes.py_object).value

# 11.2.3 使用__slots__
# __slots__节省内存
# 一个很小的类拥有很多实例可能会消耗很多内存
# 1. __slots__只对当前类的实例起作用，对继承的子类是不起作用的
# 2. 由于使用了__slots__，python不会再为实例提供__dict__属性，没有__dict__属性的实例消耗的内存就少了，
#   因为每个实例都
