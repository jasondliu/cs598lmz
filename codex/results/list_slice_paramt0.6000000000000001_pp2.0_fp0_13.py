import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
import gc
gc.collect()
c=lst[0]
print(c)
#print(len(keepali0e))
#print(keepali0e)
#print(keepali0e[0])
#print(keepali0e[0]().c)
#print(keepali0e[0]().c.c)
#print(keepali0e[1]().c)
#print(keepali0e[1]().c.c)
#print(lst)

#print(keepali0e[0]().c)
#print(keepali0e[0]().c.c)
#print(keepali0e[1]().c)
#print(keepali0e[1]().c.c)
#print(lst)
#print(keepali0e[0]().c)
#print(keepali0e[0]().c.c)
#print(keepali0e[1](
