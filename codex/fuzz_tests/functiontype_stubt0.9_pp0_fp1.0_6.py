from types import FunctionType
a = (x for x in [1])
print(type(a.__next__))
print(type(next))
print(type(a.__next__) == type(next))
print(type(a.__next__) is type(next))
print(type(a.__next__) is FunctionType)
print(type(a.__next__) is type)


a = (x for x in [1])
class A:
    b = next(a)
print(A().b, type((A.b)))
'''
(<function next>, <class 'type'>)
<class 'function'>
(<class 'function'>, <class 'type'>)
True
True
True
True
1 <class 'int'>
'''
