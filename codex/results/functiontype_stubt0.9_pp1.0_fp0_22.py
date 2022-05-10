from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(isinstance(a.__iter__, FunctionType))
# FunctionType下有一个__code__属性，属性值是另一个对象，具有co_name属性，可以获取函数名
print(a.__iter__.__code__.co_name)
# 自定义函数
d
