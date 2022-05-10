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
I want to understand the code above.
I know that the keepalive is a list of weakrefs, and the lst is a list of strings.
But I don't know what is the purpose of the while loop.
Why does the while loop add a slice of lst to the keepalive?
Why does the while loop not end?
Thank you.


A:

The callback function <code>callback()</code> deletes the first item from the list <code>lst</code>.
The code is trying to make sure that <code>lst</code> is not garbage collected by adding a reference to it in <code>keepalive</code>.  However, the reference is a slice, so it is a new list object and not the same <code>lst</code> object.  The callback function will delete the first item from <code>lst</code>, but the slice will still have the same reference to the original <code>lst</code> object.
So the while loop adds a new slice to <code>keepalive</code>, then the callback function deletes the first item from the
