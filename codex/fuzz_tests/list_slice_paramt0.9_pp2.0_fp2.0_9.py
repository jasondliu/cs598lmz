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

#the output is 1
import weakref
class A(object):pass
def callback(x=None):print "deleted"
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(lst)

#deleted
#1
import weakref
class A(object):pass
def callback(x):print "deleted"
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(lst)

##all x are callback functions
import weakref
class A(object):pass
def callback(x):x()
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(
