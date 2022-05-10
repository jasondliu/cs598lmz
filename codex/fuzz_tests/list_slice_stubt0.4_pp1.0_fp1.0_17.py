import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.c=weakref.ref(lst[0],callback)
print len(lst)
del lst
print len(keepalive)
del keepalive[0]
print len(keepalive)
