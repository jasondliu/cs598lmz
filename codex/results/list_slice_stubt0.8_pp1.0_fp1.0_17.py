import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
weakref.ref(a,callback)
weakref.ref(lst[0],callback)
keepalive.append(a)
del a
del keepalive[:]
for i in range(100):
    lst.append(str())
    keepalive.append(lst[-1])
keepalive[:]=[[]]
