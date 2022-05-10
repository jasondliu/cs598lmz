import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
lst.append(weakref.ref(a,callback))
keepali0e.append(a)
print(lst)
del a
print(lst)
lst=[]
a=A()
a.c=a
keepali0e.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
lst=[]
a=A()
a.c=a
keepali0e.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
lst=[]
a=A()
a.c=a
keepali0e.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
