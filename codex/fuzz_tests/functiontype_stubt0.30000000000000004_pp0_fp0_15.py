from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__iter__) == FunctionType)
print(type(a.__iter__) == type(a.__next__))
print(type(a.__iter__) == type(a.__next__) == FunctionType)

# 迭代器协议
# 可迭代对象：实现了__iter__方法
# 迭代器：实现了__iter__和__next__方法
# 可迭代对象和迭代器的区别：
# 可迭代对象可以被for循环，迭代器不可以
# 可迭代对象可以被iter()函数转换
