import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
d={0:a}
for i in range(len(lst)):
    lst.append(weakref.proxy(A(),callback))
    keepalive.append(lst[-1])
del lst
d[0].c=None
print([x for x in keepalive])
