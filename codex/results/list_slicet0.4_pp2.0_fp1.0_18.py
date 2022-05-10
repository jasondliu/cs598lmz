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
print(keepali0e)

print("\n")

import weakref
class A(object):pass
def callback(x):print(x)
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while keepali0e:keepali0e.append(keepali0e[:])

print("\n")

import weakref
class A(object):pass
def callback(x):print(x)
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while keepali0e:keepali0e.append(keepali0e[:])

print("\n")

import weakref
class A(object):pass
def callback(x):print(x)
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while keepali
