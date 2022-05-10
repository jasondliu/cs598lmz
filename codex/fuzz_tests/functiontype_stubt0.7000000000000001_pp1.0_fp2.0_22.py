from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])

print(type(a) is type(b))
print(isinstance(a, type(b)))

# is的优先级低于==, 不是同一个对象但是满足==的话, 会判断为相等.
print(a is b)
print(a == b)

print("\n")

# isinstance
print(isinstance(a, FunctionType))
print(isinstance(a, type(a)))
print(isinstance(a, tuple))
print(isinstance(a, type(b)))
print(isinstance(a, type(object)))
print(isinstance(a, object))

print("\n")

# type
print(type(a) is type(b))
print(type(a) is FunctionType)
print(type(a) is type(a))

print("\n")

# 一般都是使用
