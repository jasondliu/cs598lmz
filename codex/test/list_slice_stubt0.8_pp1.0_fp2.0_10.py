import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive=keepali0e
keepalive.append(a)
keepalive.append(a.b)
keepalive.append(a.c)
w=weakref.ref(a,callback)
del a
del keepali0e
print(lst)
del lst
