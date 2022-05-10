import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
print(lst[0])
del a
del keepali0e
print(lst[0])
lst=[]
print(lst)
