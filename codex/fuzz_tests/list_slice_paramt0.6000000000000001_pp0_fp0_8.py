import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print "before del a"
print lst
print "\n"
del a
print "after del a"
print lst

print "\n"

import weakref
class A(object):pass
def callback(x):print x
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print "before del a"
print lst
print "\n"
del a
print "after del a"
print lst
