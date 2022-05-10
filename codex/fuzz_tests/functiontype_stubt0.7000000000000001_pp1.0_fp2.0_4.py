from types import FunctionType
a = (x for x in [1])
print(type(a))
# <class 'generator'>

b = '[x for x in [1]]'
c = '[x for x in [1, 2]]'
print(b == c)
# False
