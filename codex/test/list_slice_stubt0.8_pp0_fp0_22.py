import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
a.other=b
b.other=a
a.wr=weakref.ref(a)
b.wr=weakref.ref(b)
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(b,callback))
lst.append(weakref.ref(a.c,callback))
lst.append(weakref.ref(a.other,callback))
lst.append(weakref.ref(a.other.other,callback))
lst.append(weakref.ref(b.other,callback))
lst.append(weakref.ref(b.other.other,callback))
lst.append(weakref.ref(a.other,callback))
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(a.other.other,callback))
lst.append(weakref.ref(a.other.other,callback))
del a
del b
import gc
gc.collect()
