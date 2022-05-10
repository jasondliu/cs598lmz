import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#2.2.2.2
import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e

#2.2.2.3
import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e()

#2.2.2.4
import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e()
print keepali0e()

#2.2.2.5
import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()

