import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
keepali0e.append(callback)
weakref.finalize(a,callback,lst)
del a
print lst
del lst
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
weakref.finalize(a,callback,lst)
del a
del keepali0e[0]
print lst
del lst
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
weakref.finalize(a,callback,lst)
del a
callback(None)
print lst
del lst
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(
