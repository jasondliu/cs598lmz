from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_names)

# 使用内建函数dir()可以获得对象的所有属性和方法
# list(dir(FunctionType(lambda: None, {})))

# 使用__dict__属性可以获取对象属性
# FunctionType(lambda: None, {}).__dict__

# 使用__slots__属性可以限制对象属性

# 使用__getattr__()和__setattr__()方法可以控制对象属性的获取和设置

# 使用__getattribute__()方法可以控制对象属性的获
