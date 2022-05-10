import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst[0]

#2
print '2'
import weakref
class A(object):pass
def callback(x):print x
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a

#3
print '3'
import weakref
class A(object):pass
def callback(x):print x
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a

#4
print '4'
import weakref
class A(object):pass
def callback(x):print x
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a

#5
print '5'
import weakref
class A(object):pass
def callback(x):print x
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a

#6
print '6'
import weakref
