import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.pop()
del a
keepali0e.pop()
del keepali0e
import gc
for x in gc.get_referrers(str):
	print x
