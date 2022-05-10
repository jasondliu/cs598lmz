import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
weakref.ref(lst[0],callback)
print lst[0]
</code>
So is there a way to put a weakref to an object inside a list and have the weakref to be called when the object is deleted?

