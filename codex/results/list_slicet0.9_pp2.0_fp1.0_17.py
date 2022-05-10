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
notices that the last wile is need so that the weakref callbacks can be trigger
i am not sure but it should be possible to modify the exemple so that the callback does nothing.
you can also have a look to : http://docs.python.org/library/weakref.html there is already a problem described as circular reference

