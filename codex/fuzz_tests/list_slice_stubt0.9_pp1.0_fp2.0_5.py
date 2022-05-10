import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
keepalive=[a]
print(list(gc.get_referrers(a)))
del a
l=['umai']
print(l)
del l
