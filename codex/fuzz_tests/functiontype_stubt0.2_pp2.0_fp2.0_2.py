from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.send))
print(type(a.throw))
print(type(a.close))

print(isinstance(a.__next__, FunctionType))
print(isinstance(a.__iter__, FunctionType))
print(isinstance(a.send, FunctionType))
print(isinstance(a.throw, FunctionType))
print(isinstance(a.close, FunctionType))

print(a.__next__.__self__)
print(a.__iter__.__self__)
print(a.send.__self__)
print(a.throw.__self__)
print(a.close.__self__)

print(a.__next__.__self__ is a)
print(a.__iter__.__self__ is a)
print(a.send.__self__ is a)
print(a.throw.__self__ is a)
print(a.close.__self__ is a
