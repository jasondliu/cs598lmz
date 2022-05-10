import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
lst.append(a)
lst.append(b)
keepalive=lst
del lst
gc.collect()
for i in range(10):
    lst=[]
    lst.append(weakref.ref(lst,callback))
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive.append(lst)
    keepalive
