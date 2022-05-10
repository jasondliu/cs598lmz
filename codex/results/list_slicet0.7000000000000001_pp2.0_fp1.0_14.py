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
print(keepali0e[0]())
#print(keepali0e[1])

#output:
#None
</code>

Explanation
<blockquote>
<p>how does this code work?</p>
</blockquote>
All is in the uncollectable cycle.
<code>a.c=a</code> makes <code>a</code> uncollectable because of the uncollectable cycle.
<code>a</code> has reference to <code>a</code> to the object <code>a</code>.
<code>a</code> object is not collectable because <code>a</code> has reference to <code>a</code> and <code>a</code> has reference to <code>a</code>.
<code>a</code> has reference to <code>a</code> and <code>a</code> has reference to <code>a</code> and <code>a</code> has reference to <code>a</code> and <code>a</code> has reference to <code>a</code> and <code
