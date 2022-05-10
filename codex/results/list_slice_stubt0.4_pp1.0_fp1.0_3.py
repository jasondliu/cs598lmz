import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a.c,callback))
print len(lst)
del a
print len(lst)
print lst[0]
del lst
print len(keepalive)
del keepalive[0]
print len(keepalive)
