import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
lst[0]=a
weakref.ref(a,lambda h:x.append(h))
callback(keepalive)
print a,len(keepalive.c),lst
