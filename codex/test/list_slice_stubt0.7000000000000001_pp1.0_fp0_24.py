import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a_ref=weakref.ref(a,callback)
lst.append(a_ref)
a=None
del keepali0e
