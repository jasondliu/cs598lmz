import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst.append(a)
del a
del keepali0e
gc.collect()
print len(lst)
print gc.collect()
print len(lst)
