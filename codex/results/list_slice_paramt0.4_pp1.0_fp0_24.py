import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
lst.append(a)
del a
print lst
print keepali0e

#[str(), <__main__.A object at 0x00000000029D8F98>, <__main__.A object at 0x00000000029D8F98>]
#[<weakref at 0x00000000029D8F60; to 'A' at 0x00000000029D8F98>]

import weakref
class A(object):pass
def callback(x):print x
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print keepali0e

#<weakref at 0x00000000029D8F60; dead>

import weakref
class A(object):pass
def callback(x):print x
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print keepali0e

