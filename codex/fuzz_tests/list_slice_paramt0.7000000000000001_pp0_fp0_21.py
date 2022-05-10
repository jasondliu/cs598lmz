import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
print(lst)

import weakref
class A(object):pass
lst=[str()]
a=A()
a.c=a
ref=weakref.ref(a.c,lambda x:lst.pop(0))
del a
print(lst)

import weakref
class A(object):pass
lst=[str()]
a=A()
a.c=a
ref=weakref.ref(a.c,lambda x:lst.pop(0))
del a
del ref
print(lst)

import weakref
class A(object):pass
lst=[str()]
a=A()
a.c=a
ref=weakref.ref(a.c,lambda x:lst.pop(0))
del a
del ref
print(lst)
