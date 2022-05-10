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
</code>


A:

You may want to use an <code>OrderedDict</code> to keep the order.
<code>&gt;&gt;&gt; d = collections.OrderedDict()
&gt;&gt;&gt; d["nigga"] = 5
&gt;&gt;&gt; d["fuck"] = "bitch"
&gt;&gt;&gt; d["this"] = True
&gt;&gt;&gt; d
OrderedDict([('nigga', 5), ('fuck', 'bitch'), ('this', True)])
</code>

