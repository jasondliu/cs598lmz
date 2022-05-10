import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(a)
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
del a
del lst
while keepali0e[0]():pass
