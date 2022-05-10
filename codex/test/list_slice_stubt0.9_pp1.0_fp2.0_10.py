import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(A())
keepali0e.append(a)
lst[0]=weakref.ref(a,callback)
len(keepali0e)==int()
