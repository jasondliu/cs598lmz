import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive.append(a)
del a
gc.collect()
del lst[0]
a=5

#now a is not referenced and should be collected, but for the following callback
gc.collect()

keepalive=lst=callback=None
gc.collect()
