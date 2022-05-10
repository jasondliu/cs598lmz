from types import FunctionType
a = (x for x in [1])
b = [1]
c = {'a': 1}
d = {'a': 1}.get
e = FunctionType
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# isinstance 判断是否是某个类型
print(isinstance(a, GeneratorType))
print(isinstance(b, list))
print(isinstance(c, dict))
print(isinstance(d, FunctionType))
print(isinstance(e, FunctionType))

# issubclass 判断是否是某个类型的子类
print(issubclass(list, object))
print(issubclass(dict, object))
print(issubclass(object, object))
print(issubclass(FunctionType, object))
