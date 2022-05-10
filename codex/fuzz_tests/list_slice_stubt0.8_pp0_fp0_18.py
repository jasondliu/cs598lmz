import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a.c
lst.append(a)
keepalive=a
clock=time.clock()
for i in range(100000):
    d= weakref.WeakKeyDictionary(dict.fromkeys(lst,lst))
    d[a]=a
    keepalive=d
    o=weakref.ReferenceType(a, callback)
    lst.append(0)
    keepalive = o
    lst.append(1)
    keepalive = o
    lst.append(2)
    keepalive = o
    lst.append(3)
    keepalive = o
    lst.append(4)
    keepalive = o
    lst.append(5)
    keepalive = o
    lst.append(6)
    keepalive = o
    lst.append(7)
    keepalive = o

clock=time.clock()-clock
print(clock)
