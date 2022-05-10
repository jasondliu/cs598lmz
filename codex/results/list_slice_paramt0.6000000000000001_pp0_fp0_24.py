import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst

#test the weak reference
del a
lst

#test the weak reference
keepalive=[]
for i in range(1,10):
    keepalive.append(weakref.ref(A(),callback))
    lst.append(str())
del keepalive
lst


#test the weak reference
keepalive=[]
for i in range(1,10):
    keepalive.append(weakref.ref(A(),callback))
    lst.append(str())
del keepalive
lst


#test the weak reference
keepalive=[]
for i in range(1,10):
    keepalive.append(weakref.ref(A(),callback))
    lst.append(str())
del keepalive
lst


#test the weak reference
keepalive=[]
for i in range(1,10):
    keepalive.append(weakref.ref(A(),callback))
    lst.append(str())
del keepalive
lst


#test the weak reference
