import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
print(lst)
lst[0]=weakref.ref(lst,callback)
print(lst)
del lst
</code>
I have a list <code>lst</code> that contains a string. I then create a circular reference with <code>a</code> and <code>a.c</code> and append it to <code>keepalive</code>. I then make <code>lst[0]</code> a weak reference to <code>lst</code> with a callback. I then delete <code>lst</code>.
I expect <code>lst</code> to be deleted, but it is not.
I am using Python 3.6.0.


A:

You are using a <code>weakref.ref</code> object, not a <code>weakref.WeakKeyDictionary</code> object. The former is a weak reference to an object, the latter is a weak reference to a key in a dictionary.
The <code>weakref.ref</code> object is a proxy for the
