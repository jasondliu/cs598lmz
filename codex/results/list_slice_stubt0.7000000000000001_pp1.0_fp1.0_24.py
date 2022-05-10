import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=weakref.WeakKeyDictionary()
a.d[a]=lst
a.e=lst
a.e.append(a)
b=A()
b.d=a.d
del a.c
a.d=None
del a.d
del a
print b.e
