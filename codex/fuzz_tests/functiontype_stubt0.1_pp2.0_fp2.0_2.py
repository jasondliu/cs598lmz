from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)

print(dir(a))
print(dir(a.__next__))
print(dir(a.__next__.__code__))
print(dir(a.__next__.__code__.co_code))
print(dir(a.__next__.__code__.co_code.__eq__))
print(dir(a.__next__.__code__.co_code.__eq__.__code__))
print(dir(a.__next__.__code__.co_code.__eq__.__code__.co_code))
print(dir(a.__next__.__code__.co_code.__eq__.__code__.co_code.__eq__))
print(dir(a.__next__.__code__.co_code.__eq__.__code__.co_code.__eq__.__
