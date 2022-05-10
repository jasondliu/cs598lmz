import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
for x in keepalive:
    lst.append(weakref.ref(x,callback))
print lst[0]
print lst[1]()
print lst[1]()
del a
print lst[0]
print lst[1]()
print lst[1]()
