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
print keepali0e
a=keepali0e.pop()
b=a()
print b
a.c=a
del a
del b
keepali0e[0]().c=keepali0e[0]()
del keepali0e
print keepali0e
'''

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
print keepali0e
keepali0e[0]().c=keepali0e[0]()
del keepali0e
print keepali0e

#Creating a reference cycle
#"Cyclic" refers to the use of circular references, where at least two objects are each holding a reference to the other, and nothing else is holding a reference to either of them.
#Example
'''
class A(object):pass

