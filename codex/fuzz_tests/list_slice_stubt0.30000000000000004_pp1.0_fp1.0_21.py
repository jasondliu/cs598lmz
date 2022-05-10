import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
for i in range(10000):
    a=A()
    a.c=a
    weakref.ref(a,callback)
    del a
    lst.append(str())
    if i%100==0:
        print(i)
print(len(lst))
