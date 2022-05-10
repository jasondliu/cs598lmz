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
print keepali0e
</code>
I am trying to understand how this code works. I know that <code>weakref.ref</code> creates a weak reference to an object. But I do not understand what is happening in the <code>while</code> loop.


A:

<code>lst</code> is a list of strings.  The first string is empty.  The <code>while</code> loop is adding all of the empty strings to <code>keepali0e</code> until <code>lst</code> is empty.  The <code>callback</code> function is called when <code>a</code> is deleted, which removes the first element from <code>lst</code>.

