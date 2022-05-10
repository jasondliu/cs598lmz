import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
a.a=a.b
keepali0e.append(a)
keepali0e.append(a.b)
keepali0e.append(a.c)
keepali0e.append(a.a)
del a
del a.b
del a.c
del a.a
del keepali0e
gc.collect()
print(lst)
