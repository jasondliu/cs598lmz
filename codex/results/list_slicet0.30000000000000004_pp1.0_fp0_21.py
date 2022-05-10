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
I am trying to understand the output of this code, which is:
<code>[[&lt;weakref at 0x7f8f4c4d4b80; to 'A' at 0x7f8f4c4d4b50&gt;], ['\x00']]
</code>
I understand that the first element of the list is a weak reference to the object A, but I do not understand why the second element is a list with a single element, which is a string of length 0.
I would appreciate any help.


A:

The <code>callback</code> function is called when the weak reference is garbage collected.  When the <code>A</code> object is deleted, it is garbage collected, and the <code>callback</code> function is called.  The <code>callback</code> function deletes the first element of <code>lst</code>, which is a string of length 0.  The <code>while</code> loop then appends the empty list to <code>keepali0e</code>.

