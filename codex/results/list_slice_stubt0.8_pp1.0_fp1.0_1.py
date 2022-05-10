import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
c=A()
c.c=b
keepalive.append(c)
lst.append(a)
lst.append(b)
lst.append(c)
lst.append(a)
lst.append(b)
lst.append(c)
lst.append(a)
lst.append(b)
del keepalive[:]
lst[0]=None
del a,b,c
lst[0]=None
gc.collect()
lst[0]=None
gc.collect()
lst[0]=None
gc.collect()
lst[0]=None
gc.collect()
lst[0]=None
gc.collect()
lst[0]=None
gc.collect()
lst[0]=None
gc.collect()
lst[0]=None
gc.collect()
lst[0]=None
gc.collect()
lst[0]=None
print len(lst)
