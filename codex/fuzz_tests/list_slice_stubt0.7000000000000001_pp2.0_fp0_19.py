import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepali0e.append(a)
keepali0e.append(a)
keepali0e.append(a)
del keepali0e
a=None
def callback():
 assert 0
gc.disable()
lst[0].c=lst
lst.append(lst)
gc.collect()
gc.collect()
gc.collect()
del lst
gc.enable()
gc.collect()
gc.collect()
gc.collect()
