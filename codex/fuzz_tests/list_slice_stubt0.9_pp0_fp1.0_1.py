import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
lst[0]=(a,a,a)
del a
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print("end")
</code>
<code>root@ubuntu:/home/zeng/gc_test# python2 test_gc.py
1
1
1
1
</code>
Why gc cannot clear lst?And when the memory is too much,what happen?


A:

It takes four times because there's four objects to collect, one in the list and three in the referenced loop. 
There are known constraints to GC on CPython and for different reasons (bugs, legacy) objects might not be collected. However, this is not the case for your program as it works on PyPy as well. 
Upon reading the source, it seems that it's in fact possible to create objects that won't be collected under CPython:

cyclic <code>classes</code> that keep their reference to themselves,
objects that implement the <code>__del__</code> method and raise an exception, or
