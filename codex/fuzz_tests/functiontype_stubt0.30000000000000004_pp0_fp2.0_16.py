from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in [1])))
print(type(FunctionType))
print(type(FunctionType(lambda x: x, {})))

# 判断是否是某种类型
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 判断是否是某个类的实例
print(isinstance([1, 2, 3], list))
print(isinstance((1, 2, 3), tuple))

# 判断是否是某个类的子类
print(issubclass(list, (list, tuple)))
print(issubclass(tuple, (list, tuple)))

# 获取对象的所有属性和方法
