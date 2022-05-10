import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
import gc
gc.collect()
print lst

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
