from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type((x for x in [1])))
print(type(lambda x: x))
print(type(FunctionType(lambda x: x, globals())))
print(type(FunctionType(lambda x: x, globals()).__call__))

print(type(iter(a)))
print(type(iter(a).__next__))
print(type(iter(a).__next__()))

print(type(iter([1, 2, 3])))
print(type(iter([1, 2, 3]).__next__))
print(type(iter([1, 2, 3]).__next__()))

print(type(iter({1, 2, 3})))
print(type(iter({1, 2, 3}).__next__))
print(type(iter({1, 2, 3}).__next__()))

print(type(iter({1: 1, 2: 2})))
print(type(iter({1: 1, 2: 2}).__next__))
print(type(iter({1: 1,
