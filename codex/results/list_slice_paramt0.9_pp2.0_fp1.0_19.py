import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
class B(set):pass
b=B()
for i in range(3):lst.append(B())
    lst[-1].add(lst[-2])
for i in range(2):lst.append(B())
    lst[-1].add(lst[-2])
b.add(lst[-1])
lst[-3].add(lst[-1])
lst=[str()]
lst.append(B())
for i in range(2):lst.append(B())
    lst[-1].add(lst[-2])
lst[-3].add(lst[-1])
lst.append(str())
lst[-2].add(lst[-1])
del lst
</code>

