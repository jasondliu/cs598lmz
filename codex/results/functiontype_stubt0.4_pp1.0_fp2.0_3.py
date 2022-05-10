from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断一个对象是否是某个类的实例
print(isinstance(a, (str, list, tuple)))

# 判断一个对象是否是另一个对象的子类
print(issubclass(list, object))

# 判断一个对象是否是另一个对象的子类或者实例
print(isinstance(list, object))

# 判断一个对象是否是另一个对象的子类或者实例
print(isinstance(list, (str, list, tuple)))

# 获取一个对
