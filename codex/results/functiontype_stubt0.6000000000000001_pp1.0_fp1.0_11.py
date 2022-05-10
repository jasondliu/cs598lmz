from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(lambda x: x, FunctionType))
print(type(FunctionType))
print(type(GeneratorType))
print(type(type))
print(type(type(1)))
print(type(type(type)))

# 类型检查可以用 isinstance() 函数

# 如果要获得一个对象的所有属性和方法，可以使用 dir() 函数，它返回一个包含字符串的 list
print(dir('abc'))

# 类似 __xxx__ 的属性和方法在 Python 中都是有特殊用途的，比如 __len__ 方法
