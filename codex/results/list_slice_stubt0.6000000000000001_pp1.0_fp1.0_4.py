import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
cb=weakref.ref(a,callback)
del a
del a.c
del keepali0e[:]
gc.collect()
print lst
