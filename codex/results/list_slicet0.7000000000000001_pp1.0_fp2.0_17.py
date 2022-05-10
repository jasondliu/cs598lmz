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
del keepali0e

#!python
import sys,weakref
class Foo(object):pass
f=Foo()
r=weakref.ref(f)
print r()
del f
print r()

#!python
import sys,weakref
class Foo(object):pass
f=Foo()
r=weakref.ref(f)
print r()
r=None
print f
del f

#!python
import sys,weakref
class Foo(object):
    pass
f=Foo()
r=weakref.ref(f)
print r()
f.bar=1
del f
print r()

#!python
import sys,weakref
class Foo(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'Foo(%s)'%self.name
foo=Foo('foo')
r=weakref.ref(foo)
print foo
print r
print r()
del foo
print r()

#!python
import sys,
