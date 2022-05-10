import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
lst.append(a)
weakref.ref(lst,callback)
lst.append(A())
keepali0e.append(lst)
