import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
print(lst)
del a
print(lst)

import weakref
class A(object):pass
class B(object):pass
a=A()
b=B()
a.b=b
b.a=a
def callback(x):print(x)
weakref.ref(a,callback)
weakref.ref(b,callback)
del a,b
