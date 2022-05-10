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
del keepali0e;del callback
</code>
The code above creates old-style class <code>A</code> with only one attribute. This attribute is a cyclic reference to <code>a</code> itself. The callback will remove the first element of <code>lst</code> when <code>a</code> is deallocated. A reasonably complex object (eg a list or list element) is stored in the first element of <code>lst</code>.
The second line from the end uses <code>keepali0e</code> to prevent <code>a</code>'s cyclic reference from being garbage-collected. Finally, the last two <code>del</code> statements delete <code>keepali0e</code> and the callback, which triggers the final deallocation of <code>a</code> and <code>lst[0]</code>. The loop is theoretically endless and will consume RAM.
<code>python -tt mem_leak_test.py</code> gives as expected:
<code>Traceback (most recent call last):
File "mem_leak_test
