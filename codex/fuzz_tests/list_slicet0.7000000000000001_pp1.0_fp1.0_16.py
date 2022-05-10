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
</code>
The Python interpreter does not crash with it. (I used Ubuntu 16.04, Python 2.7.12 and Python 3.5.2.)

