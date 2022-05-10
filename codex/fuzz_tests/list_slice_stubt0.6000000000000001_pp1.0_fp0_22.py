import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
a.wref=weakref.ref(a,callback)
print(keepali0e)
del a
print(keepali0e)
print(lst)
