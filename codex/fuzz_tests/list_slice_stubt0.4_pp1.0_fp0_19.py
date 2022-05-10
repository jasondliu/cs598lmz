import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print len(lst)
del a
del keepalive
print len(lst)
print lst[0]
print lst[1]()
