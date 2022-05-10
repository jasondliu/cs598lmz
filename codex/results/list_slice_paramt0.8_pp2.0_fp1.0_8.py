import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
b=A()
keepali0e.append(weakref.ref(b))
del keepali0e[:]
del a,b
gc.collect()
print len(gc.garbage)
</code>

