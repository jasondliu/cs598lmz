import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
b=A()
b.c=b
lst.append(b)
del b

x=lst[-1]
del lst
print 'DEAD'
