import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
gc.collect()
print lst

#[str()]

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e[0]()
gc.collect()
print lst

#[]

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=A()
a.c=a
keep
