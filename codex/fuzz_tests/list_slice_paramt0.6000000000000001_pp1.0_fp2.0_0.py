import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst
del a
print lst
for i in range(10):
    a=A()
    lst.append(a)
    del a
    print lst
print keepali0e[0]()
print lst
del lst[1]
print lst
