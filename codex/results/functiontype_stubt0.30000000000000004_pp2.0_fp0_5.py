from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

# 判断是否是某个类型可以用isinstance()判断
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))

# 类似__xxx__的属性和方法在Python中都是
