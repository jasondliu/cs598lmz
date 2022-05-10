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

#example2
class A(object):pass
def callback(x):print "callback"
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e
print keepali0e()

#example3
class A(object):pass
def callback(x):print "callback"
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e
print keepali0e()
print keepali0e()

#example4
class A(object):pass
def callback(x):print "callback"
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e
print keepali0e()
print keepali0e()
print keepali0e()

#example5
class A(object):pass
def callback(x):print "callback"
a=A()
a.c
