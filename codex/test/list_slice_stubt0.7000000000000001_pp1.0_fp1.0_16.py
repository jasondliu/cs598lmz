import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
a.lst=lst
del a
del lst
import gc;gc.disable();gc.collect()
for i in range(100):keepali0e.append(A())
