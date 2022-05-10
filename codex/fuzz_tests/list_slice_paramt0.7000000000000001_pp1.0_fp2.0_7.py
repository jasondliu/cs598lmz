import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(a.c is a)
del a
print(lst)
lst=[]
a=A()
keepali0e.append(weakref.ref(a,callback))
print(a.c is a)
del a
print(lst)
