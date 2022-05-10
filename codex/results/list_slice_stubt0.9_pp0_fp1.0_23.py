import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a.c)
lst.append(a.c)
del a,keepalive
keepalive=[]
sys.getrefcount(lst)
lst=[]
gc.collect()
#in py3.5
gc.garbage[0]
dir(gc.garbage[0])
sys.getrefcount(lst)
lst=[]
gc.collect()
#in py3.5
gc.garbage[-1]
dir(gc.garbage[-1])
gc.collect()
gc.garbage[0]
sys.getrefcount(lst)
keepalive=[]
lst=[]
for i in range(50):
    a=A()
    keepalive.append(a.c)
    lst.append(a.c)
    break
del a,keepali0e
keepalive=[]
lst=[]
for i in range(50):
    a=A()
    keepalive.append(a.c)
    lst.append(a.c
