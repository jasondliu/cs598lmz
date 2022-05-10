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
del keepali0e
</code>
I am not sure to understand why <code>print lst</code> is not executed once <code>del keepali0e</code> is called. 
In fact, as <code>keepali0e</code> is not referenced any more, I expect the interpreter to clean all objects from list, thus calling <code>callback</code> and deleting the first element from <code>lst</code>. Then the <code>while</code> condition should be false and <code>print lst</code> should be called. 
I understand that because of the cyclic reference, the interpreter does not clean the list as long as <code>del lst</code> is not called. But why the <code>while</code> condition is tested without executing <code>del keepali0e</code> ?
I would like to understand why the interpreter works this way.


A:

<code>del keepali0e</code> will only remove the reference to the list; it doesn't destroy the list object. The callback is invoked when the object that is referenced by the <code>weakref</
