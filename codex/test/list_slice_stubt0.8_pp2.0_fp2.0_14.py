import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.lst=lst
keepali0e.append(a)
w=weakref.ref(a,callback)
