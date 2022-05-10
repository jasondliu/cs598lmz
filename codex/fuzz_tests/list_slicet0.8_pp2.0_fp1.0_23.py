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

#!/usr/bin/env python

from weakref import WeakKeyDictionary
from sys import getrefcount as grc

wkd = WeakKeyDictionary()

class Foo(object):
    def __init__(self):
        self.bar = "bar"
        wkd[self] = "baz"


foo = Foo()
grc(foo)#3
grc(foo.bar)#2
del foo
grc(Foo)#2

wkd.get(Foo)#None

f = Foo()                                                                                                                                                                                                                            grc(f)#3
grc(f.bar)#2

Foo2 = Foo()
del Foo2

del Foo
f.bar
f.bar = 'bar'
f.bar
del f.bar
f.bar

f.bar = Foo()
f.bar.bar = f

del f.bar
Foo()
Foo2 = Foo()
print grc(Foo)
del Foo2

f.bar

