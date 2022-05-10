import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print lst
print len(lst)
print keepalive
print keepali0e
print a
print a.c
print a.c.c
print len(lst)
print lst
print a
print a.c
print a.c.c
del a
print len(lst)
print lst
print keepalive
print keepali0e
