import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a#make a reference cycle
lst[0]=a#make a weak reference to it
weakref.ref(a,callback)
