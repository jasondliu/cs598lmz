import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=weakref.WeakKeyDictionary()
a.d[a]=a
keepali0e.append(a)
a.e=weakref.WeakValueDictionary()
a.e[a]=a
keepali0e.append(a)
a.f=weakref.WeakSet()
a.f.add(a)
keepali0e.append(a)
wr=weakref.ref(a,callback)
del a
keepali0e[0]=lst
keepali0e[1]=wr
keepali0e[2]=callback
