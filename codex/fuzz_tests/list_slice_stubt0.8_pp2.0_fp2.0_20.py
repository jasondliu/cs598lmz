import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(a)
a=weakref.ref(lst[1],callback)
keepali0e.append(a)
lst.append(str())
keepali0e.append(lst[2])
a=A()
a.c=a
lst.append(a)
keepali0e.append(a)
lst.append(lst)
del keepali0e
#import ctypes
#ctypes.string_at(id(lst[0]),10)
