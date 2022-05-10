from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断是否为某种类型的实例
print(isinstance(a, (GeneratorType, FunctionType)))

# 判断某个类是否是另一个类的子类
print(issubclass(list, object))

# 判断一个对象是否是另一个类的实例
print(isinstance(a, list))

# 判断一个对象是否是另一个类的子类
print(issubclass(list, object))

# 获得一个对象的所有属性和方法
print(dir(a))

# 获得某个
