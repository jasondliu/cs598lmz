import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
assert str()==lst[0]
a.c=lst
assert lst[0]==lst[0]
lst[0]=weakref.ref(lst,callback)
assert lst[0]()==lst
import gc;gc.collect()
assert lst[0]()==lst
lst[0]=str()
del lst
import gc;gc.collect()
del keepalive
import gc;gc.collect()
assert not lst
assert str()==lst[0]
del lst
import gc;gc.collect()
assert not lst
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
assert str()==lst[0]
a.c=lst
import gc;gc.collect()
lst[0]=weakref.ref(lst,callback)
assert lst[0]()==lst
lst[0]=str()
del lst
import gc;gc.collect()
