import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(a)
keepalive.append(lst)
del lst
keepalive.append(a)
del a
gc.collect()
for i in range(100):
    lst=[str()]
    lst.append(A())
    lst.append(A())
    keepalive.append(lst)
    del lst
print(keepalive)
keepalive[0].append(keepalive[1])
del keepalive[1]
gc.collect()
print(keepalive)
gc.collect()
print(keepalive)
