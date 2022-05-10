import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst,callback))
del a
del lst
import gc
while keepali0e:gc.collect()
print len(keepali0e)
</code>
I am using python 2.7.6.
I am trying to understand how weakrefs work.
I am trying to understand why the code above prints 0.
I am trying to understand why the code above does not print 1.
I am trying to understand why the code above does not print 2.
I am trying to understand why the code above does not print 3.
I am trying to understand why the code above does not print 4.
I am trying to understand why the code above does not print 5.
I am trying to understand why the code above does not print 6.
I am trying to understand why the code above does not print 7.
I am trying to understand why the code above does not print 8.
I am trying to understand why the code above does not print 9.
I am trying to understand why the code above does not print 10.
I am trying to understand why the code above does not
