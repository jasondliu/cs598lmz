from types import FunctionType
a = (x for x in [1])
print(type(a))

print(type(lambda x: x))
print(type(abs))
print(type(a))

print(type(FunctionType))

print(type(type))

print(type(int))

print(type(a)==generator)

print(type(a)==FunctionType)

print(type(a)==type)


# isinstance(object, classinfo)
# 如果参数 object 是 classinfo 的实例对象或者是一个(直接、间接或虚拟)子类的实例对象则返回 True，否则返回 False。

print(isinstance(a, generator))

print(isinstance(a, FunctionType))


# issubclass(class, classinfo)
# 如果参数 class 是类对
