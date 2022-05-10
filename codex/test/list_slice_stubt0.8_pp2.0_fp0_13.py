import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keep=weakref.ref(a,callback)
lst=[A()]
lst[-1].c=lst[-1]
