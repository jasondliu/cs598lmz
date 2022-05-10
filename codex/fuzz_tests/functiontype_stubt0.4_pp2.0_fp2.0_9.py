from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a.__iter__))
print(type(a.__iter__()) == a)
print(type(a.__iter__().__next__))
print(type(a.__iter__().__next__()) == a.__iter__())
print(type(a.__iter__().__next__().__next__))
print(type(a.__iter__().__next__().__next__()) == a.__iter__().__next__())
print(type(a.__iter__().__next__().__next__().__next__))
print(type(a.__iter__().__next__().__next__().__next__()) == a.__iter__().__next__().__next__())
print(type(a.__iter__().__next__().__next__().__next__().__next__))
print(type(a.__iter__().__next__().__next__().__next__().__next__()) == a.__iter__().__next__().__next__().__next
