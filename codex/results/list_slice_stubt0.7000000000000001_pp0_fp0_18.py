import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
weakref.ref(a,callback)
del a
print len(lst)
</code>
This is the output of the code:
<code>0
</code>
But why isn't the callback triggered in this case?


A:

As stated in the documentation, weak references will not be called if the object is still referenced elsewhere:
<blockquote>
<p>Circular references which include a weakref are handled correctly:
  when the last strong reference to a child object is removed, the weak
  references to the parent are notified, and the parent’s <code>&lt;code&gt;__del__()&lt;/code&gt;</code>
  method, if any, is invoked before its weak references are cleared.</p>
</blockquote>

