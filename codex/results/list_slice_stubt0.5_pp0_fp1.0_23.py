import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(a.c,callback))
del a
del a.c
del keepali0e[:]
for i in range(2):
    print(lst)
    print(gc.collect())
