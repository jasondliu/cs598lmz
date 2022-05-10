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
lst=[]
print(lst)
print(keepali0e)
</code>


A:

When you call <code>del lst[0]</code>, the <code>lst</code> global variable is just assigned with the empty list. 
What you want to do is to exit the while loop. You can do that with a flag pretty easily:
<code>...
I_want_to_exit = False
def callback(x):
    del lst[0]
    I_want_to_exit = True
...
while lst and not I_want_to_exit:
    keepali0e.append(lst[:])
print(lst)
print(keepali0e)
</code>
Better yet, use a dead weak reference with <code>print_weakref_callback</code> and the <code>is</code> operator. You don't need to create a list or a class:
<code>x = weakref.ref(None, weakref.print_weakref_callback)
y = weakref.ref(x, weakref
