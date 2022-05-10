import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
lst[0].c=lst[0]
keepalive.append(lst)
print lst
del lst[0]
gc.collect()
print lst
print lst[0].c
keepalive.append(lst[0].c)
print lst[0].c
lst[0].c=lst[0]
print lst[0].c
print lst[0].c.c
print lst[0].c.c.c
print lst[0].c.c.c.c
print lst[0].c.c.c.c.c
print lst[0].c.c.c.c.c.c
print lst[0].c.c.c.c.c.c.c
print lst[0].c.c.c.c.c.c.c.c
print lst[0].c.c.c.c.c.c.c.c.c
print lst[0].c.c.c.c.c.c
