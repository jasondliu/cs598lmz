import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
lst.append(a)
keepalive.append(a)
keepalive.append(a.b)
keepalive.append(a.c)
del a
lst.append(weakref.ref(lst[1],callback))
del keepali0e
print(lst)
