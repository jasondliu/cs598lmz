from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

print(type(a.__iter__))
print(type(a.__iter__) == FunctionType)

print(type(a.__iter__()) == type(a))

print(type(a.__iter__().__next__))
print(type(a.__iter__().__next__) == FunctionType)

print(type(a.__iter__().__next__()) == int)

print(type(a.__iter__().__next__().__next__))
print(type(a.__iter__().__next__().__next__) == FunctionType)

print(type(a.__iter__().__next__().__next__()) == StopIteration)

print(type(a.__iter__().__next__().__next__().__next__))
print(type(a.__iter__().__next__().__next__().__next__) == FunctionType)

print(type
