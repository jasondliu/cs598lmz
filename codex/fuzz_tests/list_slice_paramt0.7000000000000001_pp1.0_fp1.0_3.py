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
for i in range(10):
    print(lst)
    print(keepali0e)
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
for i in range(10):
    print(lst)
    print(keepali0e)
