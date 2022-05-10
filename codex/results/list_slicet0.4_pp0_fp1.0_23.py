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
del keepali0e,lst
</code>
I'm trying to understand how this code works.
What I understand is that the <code>lst</code> will be deleted when the <code>a</code> is deleted.
But I don't understand why <code>lst</code> is deleted in the end.
Can anyone explain this for me?


A:

<blockquote>
<p>I don't understand why <code>&lt;code&gt;lst&lt;/code&gt;</code> is deleted in the end.</p>
</blockquote>
<code>lst</code> is not deleted in the end. The <code>lst</code> is deleted when the <code>a</code> is deleted.
<code>lst</code> is deleted because <code>a</code> is deleted.
<code>a</code> is deleted because <code>a</code> is a circular reference, and the circular reference is broken when <code>a</code> is deleted.
<code>a</code> is deleted because there is no other reference
