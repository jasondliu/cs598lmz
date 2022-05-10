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

print(a.__next__)
print(a.__iter__)
print(a.send)
print(a.throw)
print(a.close)

print(a.__next__())
print(a.__iter__())
print(a.send(None))
print(a.throw(Exception))
print(a.close())

print(a.__next__())
