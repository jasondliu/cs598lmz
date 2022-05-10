import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e[0].callback=callback
lst[0]=keepali0e[1]
del keepali0e
del a
del lst
gc.collect()
</code>

