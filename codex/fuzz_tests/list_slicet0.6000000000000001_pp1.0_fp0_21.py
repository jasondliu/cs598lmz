import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print len(keepali0e)

def callback(x):print x
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a

import weakref
class A(object):pass

a=A()
b=A()
c=A()
a.b=b
b.c=c
c.a=a
del a,b,c
import weakref
class A(object):pass

a=A()
b=A()
c=A()
a.b=b
b.c=c
c.a=a
del a,b,c

import weakref
class A(object):pass

a=A()
b=A()
c=A()
a.b=b
b.c=c
c.a=a
del a,b,c

import weakref
class A(object):pass

a=A()
b=A()
c=A()
a.b=b
b.c=c

