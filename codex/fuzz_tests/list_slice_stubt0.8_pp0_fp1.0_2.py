import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
del a,a.c
lst.append(weakref.ref(A,callback))
del keepali0e
print 'finished'
