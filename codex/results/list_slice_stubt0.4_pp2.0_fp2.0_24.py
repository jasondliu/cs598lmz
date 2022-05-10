import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
gc.collect()
print lst
print keepalive
print len(gc.garbage)

print "*"*40

class A(object):pass
def callback(x):print "callback"
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
gc.collect()
print lst
print keepalive
print len(gc.garbage)

print "*"*40

class A(object):pass
def callback(x):print "callback"
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
gc.collect()
print lst
print keepalive
print len(gc.garbage)

print "*"*40

class A(object):pass
def callback(x):print "callback"
a=A()
