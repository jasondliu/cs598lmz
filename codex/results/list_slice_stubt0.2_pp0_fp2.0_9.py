import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
weakref.ref(lst[0],callback)
del a
del keepalive
del lst
del callback
gc.collect()
</code>
I am using python 2.7.3.
I am not sure if this is a bug or not.

