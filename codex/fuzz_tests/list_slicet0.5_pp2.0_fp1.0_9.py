import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(len(keepali0e))
del keepali0e
lst=[]
for i in range(10):
    a=A()
    a.c=a
    lst.append(a)
    del a
print(len(lst))
del lst
</code>

