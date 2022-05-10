from types import FunctionType
a = (x for x in [1])
print(type(a))

b = [x for x in [1]]
print(type(b))

c = {x for x in [1]}
print(type(c))

d = {x:x for x in [1]}
print(type(d))

e = {x for x in [1]}
print(type(e))

f = FunctionType(lambda x:x, globals())
print(type(f))

g = lambda x:x
print(type(g))

h = type(lambda x:x)
print(type(h))

i = type(type(lambda x:x))
print(type(i))

print(type(i) is type)
print(type is type)

# <class 'generator'>
# <class 'list'>
# <class 'set'>
# <class 'dict'>
# <class 'set'>
# <class 'function'>
# <class 'function'>
# <class 'type'>
# <class 'type'>
# True
# False
