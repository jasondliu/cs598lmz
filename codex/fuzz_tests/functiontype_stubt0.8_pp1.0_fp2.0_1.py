from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
# print(isinstance(a, Iterable))
# print(isinstance(a, Generator))
print(isinstance(a, FunctionType))

print(isinstance([], Iterable))
print(isinstance((), Iterable))

print(isinstance({}, Iterable))
print(isinstance(set(), Iterable))



# isinstance(object, classinfo)
# 如果object是classinfo的实例对象或者是一个（直接、间接或虚拟）子类的实例对象则返回True。
# 如果object并不是给定类型的对象，那么返回False。如果classinfo是元组类型，则返回True
#
