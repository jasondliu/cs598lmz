from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(type(FunctionType))
print(type(type))
print(type(object))
print(type(int))
print(type(str))
print(type(bool))
print(type(float))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))
print(type(complex))

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

