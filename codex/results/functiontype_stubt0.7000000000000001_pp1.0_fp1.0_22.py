from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))

b = [1].__iter__()
print(type(b))
print(isinstance(b,Iterable))
print(isinstance(b,Iterator))

c = {'a':1}.__iter__()
print(type(c))
print(isinstance(c,Iterable))
print(isinstance(c,Iterator))

d = range(1)
print(type(d))
print(isinstance(d,Iterable))
print(isinstance(d,Iterator))

e = FunctionType
print(type(e))
print(isinstance(e,Iterable))
print(isinstance(e,Iterator))

f = FunctionType.__call__
print(type(f))
print(isinstance(f,Iterable))
print(isinstance(f,Iterator))

'''
<class 'generator'>
True
True
<class 'list_iterator'>
True
True
<class 'dict_keyiterator'>
True
