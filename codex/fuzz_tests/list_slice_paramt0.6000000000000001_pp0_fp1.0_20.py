import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print len(lst)
del a
print len(lst)
import weakref
class A(object):pass
def callback(x):print "callback called"
a=A()
a.c=a
r=weakref.ref(a,callback)
del a
print r()
import weakref
class A(object):pass
def callback(x):print "callback called"
a=A()
a.c=a
r=weakref.ref(a,callback)
a=None
print r()
import weakref
class A(object):pass
def callback(x):print "callback called"
a=A()
a.c=a
r=weakref.ref(a,callback)
del a
print r()
import weakref
class A(object):pass
def callback(x):print "callback called"
a=A()
a.c=a
r=weakref.ref(a,callback)
a=None
print r()
import weakref
class A(object):pass
def callback(x):print "callback called"
a
