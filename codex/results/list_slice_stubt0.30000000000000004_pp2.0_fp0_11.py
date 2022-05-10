import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
a.c=None
lst.append(weakref.ref(a,callback))
del a
print len(lst)
print lst
print keepalive
print len(keepalive)
