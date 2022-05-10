import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
lst.append(a)
lst.append(weakref.ref(a,callback))
keepalive.append(lst)
del a
del lst
gc.collect()
print "ok"

print "Test 2"
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
a.b=a
lst.append(a)
lst.append(weakref.ref(a,callback))
keepalive.append(lst)
del a
del lst
gc.collect()
print "ok"

print "Test 3"
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
a.b=a
lst.append(a)
lst.append(weakref.ref(a,
