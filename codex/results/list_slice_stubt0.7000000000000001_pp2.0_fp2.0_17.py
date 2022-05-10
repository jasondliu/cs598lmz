import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst[0]=a
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst[0]=a.c
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst[0]=a.c
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst[0]=a.c
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst[0]=a.c
def gc_collect():del lst[0]
gc.collect()
del lst[0]
