import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.callback=callback
keepali0e.append(a)
lst[0]=weakref.ref(a,callback)
del a
del callback
del lst
del keepali0e
