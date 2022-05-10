import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst[0]=weakref.ref(a,callback)
del a
for i in range(100):
    lst.append(str())
    keepali0e.append(lst[0])
del lst
del keepali0e
