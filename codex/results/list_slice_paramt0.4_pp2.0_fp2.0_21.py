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
keepali0e.append(weakref.ref(b,callback))
del a,b
lst.append(str())
del lst[0]
print len(keepali0e)
