import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst[0].__class__=weakref.WeakKeyDictionary
lst.append(a)
lst[0].__setitem__(a,callback)
del a
