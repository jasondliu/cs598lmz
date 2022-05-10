import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
a.d=a
keepali0e.append(weakref.ref(a.d,callback))
del a
x=lst[0]
lst[0]=str()
print lst
print len(keepali0e)
