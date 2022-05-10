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
I am using python 2.6.6.
I am trying to create a reference cycle. I am using a weakref to break the cycle.
I am trying to understand why the weakref callback is not called.
I am using a list to keep the weakref alive.
I am using a list to keep the object alive.
I am using a list to keep the reference cycle alive.
I am using a list to keep the reference alive.
I am using a list to keep the object alive.
I am using a list to keep the reference cycle alive.
I am using a list to keep the reference alive.
I am using a list to keep the object alive.
I am using a list to keep the reference cycle alive.
I am using a list to keep the reference alive.
I am using a list to keep the object alive.
I am using a list to keep the reference cycle alive.
I am using a list to keep the reference alive.
I am using a list to keep the object alive.
I am using a list to keep the reference cycle alive.
I am using a list to keep the reference alive.
I am using a list
