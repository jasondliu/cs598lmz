import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
keepalive.append(a)
keepalive.append(a.c)
keepalive.append(b)
del a,b

for i in range(10):
    lst[0]+=str(i)
    for j in range(10):
        lst[0]+='_'
gc.set_debug(gc.DEBUG_STATS)
gc.collect()
