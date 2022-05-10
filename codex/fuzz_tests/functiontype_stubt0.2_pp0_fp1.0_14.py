from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.send))
print(type(a.throw))
print(type(a.close))

print(isinstance(a, GeneratorType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))
print(isinstance(a, FunctionType))

print(isinstance(a.__iter__, FunctionType))
print(isinstance(a.__next__, FunctionType))
print(isinstance(a.send, FunctionType))
print(isinstance(a.throw, FunctionType))
print(isinstance(a.close, FunctionType))

print(isinstance(a.__iter__, GeneratorType))
print(isinstance(a.__next__, GeneratorType))
print(isinstance(a.send, GeneratorType))
print(isinstance(a.throw, GeneratorType))
print(isinstance(a.close, GeneratorType))

print(isinstance(a.__iter__
