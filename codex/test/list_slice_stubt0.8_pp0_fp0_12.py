import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.c=True
a.c=0x3d8
a.c=0.0
a.c=("sdfsdfsdfsdfsdfsdf",)
a.c=frozenset()
a.c="co"
a.c=enumerate(range(4))
a.c=a
a._ref=lst
keepalive=a
del a
import gc;gc.collect()
