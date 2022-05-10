import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
del a
lst.append(str())
a=A()
a.c=a
keepalive=a
lst.append(str())
lst[0].c=lst
lst[1].c=lst
lst.append(str())
lst[0]=None
lst[1]=None
del lst
gc.collect()
del keepalive
gc.collect()
print 'OK'
