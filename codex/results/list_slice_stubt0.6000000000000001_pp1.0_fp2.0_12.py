import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
print(lst)
keepali0e.append(a)
del a
print(lst)

lst.append(a)
print(lst)

lst.append(A())
print(lst)

lst.append(weakref.ref(A(),callback))
print(lst)
