from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.send))
print(type(a.throw))
print(type(a.close))

print(a.__iter__ == a.__next__)
print(a.__next__ == a.send)
print(type(a.__next__) == FunctionType)
print(type(a.send) == FunctionType)

print(a.__iter__ == a.__next__)
print(a.__next__ == a.send)
print(a.__next__ == a.throw)
print(a.__next__ == a.close)

print(a.__iter__ == a.__next__ == a.send == a.throw == a.close)
print(a.__iter__ == a.__next__ == a.send == a.throw == a.close == FunctionType)

print(a.__iter__.__name__ == a.__next__.__name__ == a.send.__
