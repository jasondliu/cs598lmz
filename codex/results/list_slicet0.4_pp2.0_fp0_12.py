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
print keepali0e
</code>
I was trying to create a reference cycle. But I don't understand why the list is not empty at the end.
I am using Python 2.7.3 on Windows.

