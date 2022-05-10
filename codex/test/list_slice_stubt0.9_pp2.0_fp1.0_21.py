import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
a.l=weakref.ref(b,callback)
lst.append(b)
del b
lst.append(A())
del lst[1:]
lst.append(A())
