import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])"
</code>
But is there another way to do this?


A:

<code># -*- coding: utf-8 -*-

import weakref

class A(object): pass

values = []
a = A()
r = weakref.ref(a, lambda x: values.append(1))
del a
assert values == [1]
</code>

