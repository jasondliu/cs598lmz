from types import FunctionType
a = (x for x in [1])
print(type(a))
# <class 'generator'>

b = (1 for x in [1])
print(type(b))
# <class 'generator'>

c = (int(x) for x in ['1', '2'])
print(type(c))
# <class 'generator'>

d = (int(x) for x in ['1', '2'])
print(type(d))
# <class 'generator'>

print(isinstance(a,Iterable))
# True
print(isinstance(a,Iterator))
# True

print(isinstance(b,Iterable))
# True
print(isinstance(b,Iterator))
# True

print(isinstance(c,Iterable))
# True
print(isinstance(c,Iterator))
# True

print(isinstance(d,Iterable))
# True
print(isinstance(d,Iterator))
# True

print(isinstance(a,list))
# False
print(isinstance(b,list))
# False
print(isinstance(
