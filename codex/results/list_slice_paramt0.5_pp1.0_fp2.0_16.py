import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(len(lst))

import weakref
class A(object):pass
a=A()
a.c=a
b=A()
b.c=b
keepalive=[]
keepalive.append(weakref.ref(a,lambda x:print('a')))
keepalive.append(weakref.ref(b,lambda x:print('b')))
del a
del b

import weakref
class A(object):pass
a=A()
a.c=a
b=A()
b.c=b
keepalive=[]
keepalive.append(weakref.ref(a,lambda x:print('a')))
keepalive.append(weakref.ref(b,lambda x:print('b')))
del a
del b

import weakref
class A(object):pass
a=A()
a.c=a
keepalive=[]
keepalive.append(weakref.ref(a,lambda x:print('a')))
del a

import weakref
class A(
