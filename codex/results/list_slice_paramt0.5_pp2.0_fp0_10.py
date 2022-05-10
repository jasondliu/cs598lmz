import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print a.c
del a
print lst
print keepali0e
print len(keepali0e)
lst[0]='a'
print lst
print keepali0e
print len(keepali0e)

print '-------------------------------------'

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print a.c
del a
print lst
print keepali0e
print len(keepali0e)
lst[0]='a'
print lst
print keepali0e
print len(keepali0e)

print '-------------------------------------'

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref
