import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(weakref.ref(a,callback))
keepalive.append(lst)

b=A()
b.c=b
lst.append(b)
lst.append(weakref.ref(b,callback))
keepalive.append(lst)

c=A()
c.a=a
c.b=b
lst.append(c)
keepalive.append(lst)
del b,a
del lst[0]
del lst[1]
lst=str()
