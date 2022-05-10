import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(lst[0],callback))
del a,lst
gc.collect()
print len(keepali0e)
print keepali0e[0]()
print keepali0e[1]()
print keepali0e[2]()
