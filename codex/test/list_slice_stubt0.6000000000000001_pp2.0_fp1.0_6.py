import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
a.b=b
lst.append(a)
lst.append(b)
lst.append(a)
lst.append(b)
del a,b
lst[1]=weakref.ref(lst[1],callback)
lst[3]=weakref.ref(lst[3],callback)
