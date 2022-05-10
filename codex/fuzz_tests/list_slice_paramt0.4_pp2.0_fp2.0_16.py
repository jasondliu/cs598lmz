import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
for i in range(1000):
    print(len(lst))
    lst.append(str())
    lst.append(str())
    lst.append(str())
    del lst[:]
    lst.append(str())
    lst.append(str())
    lst.append(str())
