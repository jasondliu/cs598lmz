import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.p=a
a.t=a
a.m=A()
a.m.i=A()
a.e=a
a.m.i.t=a
lst.append(lst)
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.p,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(a.m,callback))
keepali0e.append(weakref.ref(a.e,callback))
keepali0e.append(weakref.ref(a.m.i,callback))
keepali0e.append(weakref.ref(a.m.i.t,callback))
del a
del keepali0e

# overwrite __reduce_ex__ on user-defined class
# class A(object):
#     __module__=None
#     def __reduce_ex__(self,protocol):
#         return (__import__,('
