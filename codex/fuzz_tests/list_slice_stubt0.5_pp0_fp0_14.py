import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
del a.c
print len(lst)
lst[0]=weakref.ref(lst,callback)
print len(lst)
del lst
print len(keepalive)
