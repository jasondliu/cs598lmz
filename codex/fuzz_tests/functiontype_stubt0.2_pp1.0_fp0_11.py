from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__iter__()) == a)
print(type(a.__iter__) == FunctionType)
print(type(a.__iter__()) == FunctionType)

# 判断一个对象是否是函数
print(callable(a))
print(callable(a.__iter__))
print(callable(a.__iter__()))

# 查看对象的方法
print(dir(a))
print(dir(a.__iter__))
print(dir(a.__iter__()))

# 查看对象的属性
print(hasattr(a, '__iter__'))
print(hasattr(a.__iter__, '__iter__'))
print(hasattr(a.__iter__(), '__iter__'))

# 获取对象的属性

