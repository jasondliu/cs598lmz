from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))
print(a.__next__())
print(a.__next__())

print(a.send(None))
print(a.send(None))

print(a.close())
print(a.send(None))

a = (x for x in [1])
print(a.__next__())
print(a.__next__())

print(a.throw(StopIteration))
print(a.throw(StopIteration))

b = (x for x in [1])
print(b.throw(Exception))
