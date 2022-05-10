import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print len(lst)
a=None
print len(lst)
keepali0e.append(str())
del keepali0e[0]
print len(lst)
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print len(lst)
a=None
print len(lst)
keepali0e.append(str())
del keepali0e[0]
print len(lst)
from weakref import WeakKeyDictionary
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(WeakKeyDictionary({a:callback}))
print len(lst)
a=None
print len(lst)
keepalive.append(str())
del keepalive[
