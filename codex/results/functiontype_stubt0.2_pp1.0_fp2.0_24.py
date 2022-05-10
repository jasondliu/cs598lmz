from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__()))
print(type(a.__next__().__iter__))
print(type(a.__next__().__next__))
print(type(a.__next__().__next__()))

print(type(a.__next__().__next__().__iter__))
print(type(a.__next__().__next__().__next__))
print(type(a.__next__().__next__().__next__()))

print(type(a.__next__().__next__().__next__().__iter__))
print(type(a.__next__().__next__().__next__().__next__))
print(type(a.__next__().__next__().__next__().__next__()))

print(type(a.__next__().__next__().__next__().__next__().__iter__))
print(type(a.__next__
