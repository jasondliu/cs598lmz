import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst
</code>
The above code will not delete the <code>str()</code> object in the list <code>lst</code>, but if I change the <code>str()</code> to a <code>int()</code> or <code>list()</code>, the <code>int()</code> or <code>list()</code> object will be deleted.
Why is this?


A:

<code>str()</code> is a special case. It creates an empty string object, which is a singleton. There is only one empty string in memory at a time.
The <code>weakref.ref()</code> callback is called when the referent is no longer in use, and is about to be garbage collected. The empty string is never garbage collected, because it is a singleton.
Your <code>int()</code> and <code>list()</code> objects are not singletons, and are garbage collected when the last reference to them is removed.

