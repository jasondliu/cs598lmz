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
del keepali0e[:]
lst=[]
for i in range(10):
    lst.append([1]*10*1024*1024)
    lst.append(str())
</code>

