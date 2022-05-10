from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.send))
print(type(a.throw))
print(type(a.close))

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))

print(isinstance(a.__iter__, FunctionType))
print(isinstance(a.__next__, FunctionType))
print(isinstance(a.send, FunctionType))
print(isinstance(a.throw, FunctionType))
print(isinstance(a.close, FunctionType))

print(isinstance(a.__iter__, MethodType))
print(isinstance(a.__next__, MethodType))
print(isinstance(a.send, MethodType))
print(isinstance(a.throw, MethodType))
print(isinstance(a.close, MethodType))

print(isinstance(a.__iter__, Builtin
