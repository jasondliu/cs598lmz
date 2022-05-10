import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst[0]=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
del a
print(lst)
print(keepali0e)
#print(lst[0])
print(keepali0e[1]())
print(keepali0e[2]())

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst[0]=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
del a
print(lst)
print(keepali0e)
#print(lst[0])
print(keepali0e[1]())
print(keepali0e[2]())


import weakref
class A(object):pass
def callback
