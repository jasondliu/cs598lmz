import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst
from weakref import *
class A(object):pass
class B(object):pass
a=A()
b=B()
a.b=b
b.a=a
ba=weakref.ref(a)
bb=weakref.ref(b)
print ba,bb
del a
del b
print ba,bb
print bb(),ba()
