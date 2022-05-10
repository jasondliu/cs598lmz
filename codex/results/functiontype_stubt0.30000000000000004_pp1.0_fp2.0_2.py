from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断是否是某种类型
print(isinstance(a, (GeneratorType, FunctionType)))

# 查看对象的所有属性
print(dir(a))

# 查看对象的所有方法
print(dir(a.__next__))

# 查看对象的所有方法和属性
print(dir(a.__next__))

# 查看对象的所有方法和属性
print(dir(a.__next__))

# 查看对象的所有方法和属性
print(dir(a.__next__))

# 查看对
