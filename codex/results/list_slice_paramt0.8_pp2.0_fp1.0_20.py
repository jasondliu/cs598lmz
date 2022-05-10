import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
a.c=None
gc.collect()
print lst
lst=[str()]
a.c=a
a.c=None
gc.collect()
print lst
