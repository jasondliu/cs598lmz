import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a
print lst

print '----------------------------------------------'
lst=['hello', 'world']
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a
print lst

import weakref
class A(object):pass
def callback(x):lst[0]='goodbye'
lst=['hello']
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a
print lst

import weakref
class A(object):pass
def callback(x):print 'callback'
lst=['all', 'is', 'well']
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a
del lst[1]
print lst
print '----------------------------------------------'

import weakref
class A(object):pass
def callback(x):print 'callback'
lst=['all', 'is', 'well']
a=A()
