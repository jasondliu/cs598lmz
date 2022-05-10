import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst

import weakref
class A(object):pass
a=A()
b=A()
a.b=b
b.a=a

print(a.b)
print(b.a)

del b
print(a.b)

import weakref
class A(object):pass
a=A()
b=A()
a.b=b
b.a=a

print(a.b)
print(b.a)

del b
print(a.b)

import weakref
class A(object):pass
a=A()
b=A()
c=A()
a.b=b
b.a=a
b.c=c
c.a=a
c.b=b

print(a.b)
print(b.a)
print(b.c)
print(c.a)
print(c.b)

del b
print(a.b)
print(c.a)
print(c.b)

import weakref
class
