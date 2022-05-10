import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
wr=weakref.ref(lst[0],callback)
print wr
print wr()
print lst
lst=None
print wr()
del wr
