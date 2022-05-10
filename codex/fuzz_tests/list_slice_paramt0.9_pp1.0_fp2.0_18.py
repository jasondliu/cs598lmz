import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
l=lst[0]
m=l+'a'
tmpo=keepali0e[0]()
tmpo.c=A()
tmpo.c.c=A()
tmpo.c.c.c=tmpo
gc.collect()
p=keepali0e[0]()
if p is None:raise Exception,'not updated'
str(a)
str(keepali0e[0]() is None)
lst[0]
