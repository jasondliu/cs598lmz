import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(lst)
keepali0e.append(weakref.ref(a,callback))
del keepali0e
print len(lst)

import weakref
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(lst)
keepali0e.append(weakref.ref(a,callback))
del keepali0e
print len(lst)

import weakref
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(lst)
keepali0e.append(weakref.ref(a,callback))
del keepali0e
print len(lst)

import weakref
def callback(x):del l
