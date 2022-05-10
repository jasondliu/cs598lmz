import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepali0e.append(weakref.ref(lst[0],callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del lst
```
There is an instance of A, a, and an alias to that instance, a.c. Both a and
a.c are weakrefs, but their ref objects are in a list, lst, which is itself a
weakref. Finally, a's ref object is the weakref target of a.c's ref object. All
of this is done just to keep the ref objects alive so they can be called when
the a ref object is deleted.

When Python deletes a ref object, its callback is called, if any. This can
induce more ref objects to be deleted, and more callbacks to be called, as in
this case. Because a's ref object is the callback target of a.c's ref object,
the callback for a.c's ref object is called when a's ref object is deleted.
This means lst[0] is deleted, and the callback of lst[0
