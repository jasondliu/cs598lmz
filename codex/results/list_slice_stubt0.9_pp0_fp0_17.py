import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
a.c=lst
keepaive.append(a)
del keepaive[0]
del keepali0e[:]
a=None
lst.append(a)
import gc
gc.disable()
gc.collect()
gc.enable()
print lst
print lst[0]
print type(lst[0])
print lst[0] is None
print lst is lst[0]
print len(lst[0])
