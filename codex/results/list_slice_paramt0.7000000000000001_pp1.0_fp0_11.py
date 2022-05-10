import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
print len(lst)
print keepali0e
print lst
print a.c
print weakref.ref(a) in keepali0e
print keepali0e
print weakref.ref(a,callback) in keepali0e
print keepali0e
print lst
print a.c
print keepali0e
print lst
print a.c
print a.c
print a.c
print a.c
print len(lst)
print keepali0e
