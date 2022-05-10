import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepali0e.append(a)
keepali0e.append(a.a)
keepali0e.append(a.b)
keepali0e.append(a.c)
del a
del keepali0e
lst.append(weakref.ref(lst,callback))
lst.append(weakref.ref(lst))
print lst
del lst[1:]
print lst
```

This will print:

```
['', <weakref at 0x10b5c5f90; to 'list' at 0x10b5c63d0>, <weakref at 0x10b5c5fd0; dead>]
['', <weakref at 0x10b5c5f90; dead>]
```

So the second callback never gets called, because the weakref is dead by the time we remove the first weakref.

This is problematic because it prevents the use of cycle collecting callback and weakrefs in general. For example, I have a class that stores a collection of weak
