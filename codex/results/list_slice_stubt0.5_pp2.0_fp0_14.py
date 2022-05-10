import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
weakref.ref(lst,callback)
del lst
keepalive.remove(a)
print "OK"
</code>
This code does not print anything.
I think that the problem is that the object <code>a</code> is still referenced by <code>keepalive</code>, so it is not deleted.
How can I delete the object <code>a</code>?
I did not find any function to do this.
I did not find any function to delete the reference of <code>a</code> in <code>keepalive</code>.
I tried to do:
<code>del keepalive[0]
</code>
But this does not work.


A:

You cannot remove an object from a list by deleting the list entry. You must delete the object itself:
<code>del keepalive[0]
</code>
will not remove the object from the list, it will only delete the list entry at index 0. The object itself is still in the list.
What you want is:
