import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
weakref.ref(a,callback)
del a
del keepali0e[0]
</code>
This code should run in Python 2.x or 3.x.
The code creates a circular reference and then tests if a weak reference is able to break the reference.
The result is that the weak reference is not called (the callback is not called).
This code is based on code from this answer.
This code is equivalent to the following code:
<code>import weakref
class A(object):pass
def callback(x):print('callback called')
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
weakref.ref(a,callback)
del a
del keepali0e[0]
</code>
Which prints "callback called".
Why are the two codes different? How can I get weak references to work for circular references?

