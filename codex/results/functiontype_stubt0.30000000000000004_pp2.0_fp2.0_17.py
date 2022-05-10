from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(type(a.__iter__()))
print(isinstance(a.__iter__(), GeneratorType))
print(isinstance(a.__iter__(), FunctionType))

print(type(a.__next__()))
print(isinstance(a.__next__(), GeneratorType))
print(isinstance(a.__next__(), FunctionType))

print(type(a.send))
print(isinstance(a.send, GeneratorType))
print(isinstance(a.send, FunctionType))

print(type(a.throw))
print(isinstance(a.throw, GeneratorType))
print(isinstance(a.throw, FunctionType))

print(type(a.close))
print(isinstance(a.close, GeneratorType))
print(isinstance(a.close, FunctionType))

print(type(a.gi_frame))
print(isinstance(a.gi_frame, GeneratorType))
print(isinstance
