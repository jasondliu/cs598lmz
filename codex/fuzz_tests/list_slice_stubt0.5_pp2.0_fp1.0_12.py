import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
del keepalive
