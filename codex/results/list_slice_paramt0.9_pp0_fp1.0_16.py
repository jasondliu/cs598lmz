import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a2=A()
a2.c=a2
keepali0e.append(weakref.ref(a2,callback))
lst=[a,a2,str()]
del a,a2,lst,keepali0e
print(A.__module__)
