import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
del a
del lst
print(keepali0e)
</code>
The result is:
<code>[&lt;weakref at 0x7f4e4e4d7f70; to 'A' at 0x7f4e4e4d7f10&gt;]
</code>
Why the first <code>weakref</code> is not callbacked?


A:

The documentation for <code>weakref.ref</code> states:
<blockquote>
<p>If <code>&lt;code&gt;callback&lt;/code&gt;</code> is specified, it will be called with the weak reference as its only argument when the referent is about to be finalized. The callback is called at most once and is not called if the weak reference is dead when <code>&lt;code&gt;callback&lt;/code&gt;</code> is registered.</p>
</blockquote>
The key phrase here is "
