import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
</code>


A:

You need to use <code>slicing</code>:
<code>&gt;&gt;&gt; del lst[0:1]
</code>
here <code>del lst[0]</code> is removing the item at index <code>0</code>.
<code>del lst[0:1]</code> is removing all the items from index <code>0</code> to <code>1</code>. In this case, there is only one item present. So the above code is removing that one item.
From documentation:
<blockquote>
<p>There is also another way of deleting an entire slice rather than a
  single index. This is done by specifying the first index to be
  deleted, but leaving out the second. For example:</p>
</blockquote>
<code>&gt;&gt;&gt; a = [-1, 1, 66.25, 333, 333, 1234.5]
&
