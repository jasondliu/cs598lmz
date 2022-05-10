import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
while lst:pass
</code>
I do not understand why the loop doesn't exit, since the weakref callback is called and the list is modified.

