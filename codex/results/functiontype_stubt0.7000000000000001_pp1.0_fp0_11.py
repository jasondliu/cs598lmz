from types import FunctionType
a = (x for x in [1])
b = (y for y in [2])
print(type(a))
print(type(b))
print(type(a.__next__))
print(type(b.__next__))
print(type(b.__next__) is type(a.__next__))
print(a.__next__ is b.__next__)
print(FunctionType(a.__next__))
print(FunctionType(b.__next__))
print(FunctionType(b.__next__) is FunctionType(a.__next__))

print('-----------------------------------------------------------------------')
print('--------------------------------------------------
