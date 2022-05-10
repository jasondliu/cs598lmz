import types
types.MethodType(print,())

o=object()

def f(self):
    print('hello world')

types.MethodType(f,o)

o.f=types.MethodType(f,o)

o.f()

#给实例绑定的方法，只对当前实例起作用，对其他实例是不起作用的
o2=object()
# o2.f() #AttributeError: 'object' object has no attribute 'f'

def f(self,x):
    return x

from types import MethodType
s.set_age=MethodType(f,s)
s.set_age(25)
s.age
