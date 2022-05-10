import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
lst=[]
a=A()
def callback(x):lst.append(1)
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
