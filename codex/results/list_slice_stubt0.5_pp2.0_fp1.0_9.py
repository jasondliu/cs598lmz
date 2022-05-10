import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
del keepalive
for i in range(10000):
    lst.append(str())
    lst[i].callback=callback
    lst[i].wr=weakref.ref(lst[i])
    lst[i].wr()
    del lst[i].wr
    del lst[i].callback
print len(lst)
del lst[:]
print len(lst)
