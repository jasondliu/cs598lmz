import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
for x in range(1000):
    keepali0e.append(weakref.ref(a,callback))
    a=A()
    a.c=a
    lst.append(str())
    if x%100==0:
        print(len(lst))
        print(len(keepali0e))
