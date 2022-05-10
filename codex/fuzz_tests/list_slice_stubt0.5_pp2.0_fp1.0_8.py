import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
weakref.ref(lst[0],callback)
del a
del keepalive
del keepalive0
import gc
gc.collect()
len(lst)

from weakref import WeakKeyDictionary
class C(object):pass
c1=C()
c2=C()
c3=C()
w=WeakKeyDictionary()
w[c1]=1
w[c2]=2
w[c3]=3
print w.items()
del c1
print w.items()
del c2
print w.items()
del c3
print w.items()

from weakref import WeakKeyDictionary
class C(object):pass
c1=C()
c2=C()
c3=C()
w=WeakKeyDictionary()
w[c1]=1
w[c2]=2
w[c3]=3
print w.items()
del c1
print w.items()
del c2
print w.items()
del c3
print
