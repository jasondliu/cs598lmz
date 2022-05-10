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
</code>
and here is the code which easily avoids the error (but it's not what I want):
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
del a
keepali0e.append(lst[:])
print(len(keepali0e))
</code>
I can't understand why this code return the error. Does it mean that the callback function is called only after the last cycle of the while loop?

