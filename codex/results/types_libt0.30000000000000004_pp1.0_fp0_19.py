import types
types.MethodType(lambda self, x: self.x + x, None, A)

# TypeError: unbound method &lt;lambda&gt;() must be called with A instance as first argument (got nothing instead)
</code>
So, how can I create a method on the fly?


A:

You can use <code>types.MethodType</code> to create a bound method:
<code>&gt;&gt;&gt; import types
&gt;&gt;&gt; class A(object):
...     def __init__(self):
...         self.x = 5
...
&gt;&gt;&gt; a = A()
&gt;&gt;&gt; a.add = types.MethodType(lambda self, x: self.x + x, a, A)
&gt;&gt;&gt; a.add(10)
15
</code>

