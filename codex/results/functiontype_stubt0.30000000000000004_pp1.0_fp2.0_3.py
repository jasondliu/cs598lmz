from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x: x for x in [1]}
e = {x: x for x in [1] if x > 0}
f = FunctionType(lambda: None, {})

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))

# <generator object <genexpr> at 0x7f8f2d2c2a40> <class 'generator'>
# [1] <class 'list'>
# {1} <class 'set'>
# {1: 1} <class 'dict'>
# {1: 1} <class 'dict'>
# <function <lambda> at 0x7f8f2d2c2b70> <class 'function'>

print(a.__class__)
print(b.__class__)
print(c.__class__)
print(d
