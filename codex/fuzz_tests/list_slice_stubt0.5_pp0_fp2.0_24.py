import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
a=None
keepali0e.append(lst[0])
lst[0]=weakref.ref(lst[0],callback)
lst[0]()
del lst[0]
print(keepali0e)
