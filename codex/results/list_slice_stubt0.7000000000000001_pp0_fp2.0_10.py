import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
lst[0]=weakref.ref(a, callback)
del a
print(len(lst))

# Try to trigger an assertion in weakrefobject.c by creating a new weakref
# on top of an existing one.

import weakref
class A(object): pass
class B(object): pass
def callback(x): pass
a=A()
b=B()
a.b=b
b.a=a
x=weakref.ref(b, callback)
y=weakref.ref(b, callback)
z=weakref.ref(b, callback)
del a
del b
del x
print('OK')

# Test that a new weakref on top of an existing one that has a callback
# doesn't cause a crash.
class C(): pass
class D(): pass
def callback(x): pass
c=C()
d=D()
c.d=d
d.c=c
x=weakref.ref(d, callback)
y=weakref.ref(
