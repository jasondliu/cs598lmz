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
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(b,callback))
lst.append(weakref.ref(c,callback))
del a
del b
del c
keepali0e.append(lst[0])
keepali0e.append(lst[1])
keepali0e.append(lst[2])
del lst
