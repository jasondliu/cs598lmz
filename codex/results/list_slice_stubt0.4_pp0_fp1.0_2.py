import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive.append(a)
keepalive.append(a.c)
keepalive.append(a.d)
keepalive.append(lst)
keepalive.append(lst[0])
w=weakref.ref(a,callback)
del a
del keepalive[:]
print lst
print lst[0]
print w
