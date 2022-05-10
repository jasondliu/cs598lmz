import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
weakref.ref(a,callback)
del a
print len(lst)
print lst

keepalive=[]
lst=[]
for i in range(10):
    a=A()
    a.c=a
    keepalive.append(a)
    lst.append(a)
    del a
print len(lst)
print lst

keepalive=[]
lst=[]
for i in range(10):
    a=A()
    a.c=a
    keepalive.append(a)
    lst.append(weakref.ref(a))
    del a
print len(lst)
print lst

keepalive=[]
lst=[]
for i in range(10):
    a=A()
    a.c=a
    keepalive.append(a)
    lst.append(weakref.ref(a,callback))
    del a
print len(lst)
print lst


keepalive=[]
l
