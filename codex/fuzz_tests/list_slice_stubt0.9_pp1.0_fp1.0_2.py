import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
del keepali0e
a.c=None
setattr(A,"c",lst)
A.cb=A
cb=weakref.ref(A.cb,callback)
del A
del cb
