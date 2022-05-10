from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(b) == FunctionType)
print(type(a) is FunctionType)
print(type(b) is FunctionType)
print(type(a) == type(FunctionType))
print(type(b) == type(FunctionType))
print(type(a) is type(FunctionType))
print(type(b) is type(FunctionType))

# <generator object <genexpr> at 0x7f8c9c0b8d58>
# <generator object <genexpr> at 0x7f8c9c0b8d58>
# True
# False
# <class 'generator'>
# <class 'generator'>
# True
# False
# False
# False
# False
# False
# False
#
