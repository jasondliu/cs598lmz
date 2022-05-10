import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
b=A()
lst.append(lst)
del lst
ref=weakref.ref(a)
ref2=ref()
a.a.b=ref2.c
lst = [a,ref(),callback,a]
