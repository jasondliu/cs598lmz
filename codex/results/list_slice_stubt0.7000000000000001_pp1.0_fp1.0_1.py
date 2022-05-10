import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
c=A()
c.c=c
lst.append(a)
lst.append(a)
lst.append(a)
del a
keepalive.append(b)
keepalive.append(c)
lst.append(b)
lst.append(b)
lst.append(b)
lst.append(b)
lst.append(b)
lst.append(c)
lst.append(c)
lst.append(c)
lst.append(c)
lst.append(c)
keepalive.append(lst)
lst.append(weakref.ref(lst,callback))
print len(lst)
