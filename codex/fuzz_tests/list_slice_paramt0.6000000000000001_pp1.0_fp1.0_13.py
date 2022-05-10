import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
b=A()
b.c=b
keepali0e.append(weakref.ref(b.c,callback))
del b
print(lst)
for i in range(10):
    c=A()
    c.c=c
    keepali0e.append(weakref.ref(c.c,callback))
    del c
print(lst)
del keepali0e
print(lst)
