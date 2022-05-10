import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
del a
lst[0]=a
keepalive=[a,lst[0]]
del a
collect()
del keepalive[:]
collect()
print keepalive
lst=[1,2,3]
del lst[0]
print lst
a=A()
a.c=a
del a
lst[1]=a
keepalive=[a,lst[1]]
del a
collect()
del keepalive[:]
collect()
print keepalive
lst=[1,2,3]
del lst[0]
lst[1]=a
keepalive=[a,lst[1]]
del a
collect()
del keepalive[:]
collect()
print keepalive
lst=[1,2,3]
del lst[0]
lst[1]=a
keepalive=[a,lst[1]]
del a
collect()
del keepalive[:]
collect()
print keepalive
lst=[1,2,3]
del lst[0]
lst[1]=
