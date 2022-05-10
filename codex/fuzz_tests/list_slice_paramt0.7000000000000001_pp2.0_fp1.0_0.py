import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
keepalive=[]
lst=[str()]
a=A()
keepalive.append(weakref.ref(a,callback))
print(lst)
keepalive=[]
lst=[str()]
a=A()
keepalive.append(weakref.ref(a))
print(lst)
keepalive=[]
lst=[str()]
a=A()
keepalive.append(weakref.ref(a,callback))
del lst[0]
print(lst)
keepalive=[]
lst=[str()]
a=A()
keepalive.append(weakref.ref(a,callback))
a.c=a
del lst[0]
print(lst)
keepalive=[]
lst=[str()]
a=A()
keepalive.append(weakref.ref(a,callback))
a.c=a
del a
del lst[0]
print(lst)
keepalive=[]
lst=[str
