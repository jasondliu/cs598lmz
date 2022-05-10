import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
for i in range(100):
    lst.append(lst[-1]+str(i))
    lst.append(lst[-1]+str(i))
    del lst[0]
</code>

