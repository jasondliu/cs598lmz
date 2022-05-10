import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:
    s=lst[0]
    print s
    del lst[0]
</code>
The memory for <code>a</code> should, IMO, eventually be released because one of the cyclic references (from <code>a.c</code> to <code>a</code>) is a weakref that is also referenced by a keepalive, but the address of <code>a</code> is never being printed.
Any ideas?


A:

Even if I set <code>gc.collect()</code> in Python console.
<code>&gt;&gt;&gt; import gc
&gt;&gt;&gt; gc.collect()
</code>
A object (a.c) will be freed.
And I think <code>list</code> is weakrefable cause I can't find <code>list</code> in __weakref__ list.
And a code that doesn't free object.
<code>import gc
import sys

class A(object):
    pass

def callback
