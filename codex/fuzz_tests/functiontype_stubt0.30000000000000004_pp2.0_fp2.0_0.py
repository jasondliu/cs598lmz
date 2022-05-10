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

print(type(a.__iter__().__next__()) == type(a.__iter__().__next__))

print(type(a.__iter__().__next__().__iter__))
print(type(a.__iter__().__next__().__iter__) == FunctionType)

print(type(a.__iter__().__next__().__iter__()) == type(a.__iter__().__next__().__iter__))

print(type(a.__iter__().__next__().__iter__().__next__))
print(type(a.__iter__
