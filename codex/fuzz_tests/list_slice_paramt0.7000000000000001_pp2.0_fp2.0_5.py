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

print(3*"----")

lst=[str()]
keepali0e=[]
def callback(x):del lst[0]
a=A()
keepali0e.append(weakref.ref(a,callback))
print(lst)
a.c=a
del a
print(lst)
