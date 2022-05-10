import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
print(lst)
del a
print(lst)
keepali0e.append(weakref.ref(a,callback))
del keepali0e[0]
print(lst)
del keepali0e[0]
print(lst)
