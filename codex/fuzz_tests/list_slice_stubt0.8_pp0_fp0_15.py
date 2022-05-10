import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
functools.update_wrapper(callback,A.c)
lst.append(weakref.ref(lst,callback))
</code>
I think I know what's going on in the <code>test</code> function. but I don't understand <code>test1</code> function.
In <code>test</code> function, the <code>lst</code> contains <code>str()</code>, so it's not empty. In <code>test1</code> function, <code>weakref.ref</code> will call the callback, and <code>lst</code> will be empty, so the <code>except</code> block will be executed.
But why in <code>test1</code> function, <code>lst</code> is empty first, then <code>lst</code> contains <code>str()</code>, then <code>lst</code> is empty again?


A:

The code you're looking at is found in:

https://github.com/python/cpython/blob
