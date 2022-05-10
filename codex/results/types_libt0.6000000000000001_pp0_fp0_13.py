import types
types.MethodType(lambda self: self.foo, None)
</code>
I don't understand what the first argument is and why it is a function that takes only one argument and returns a string.


A:

The first argument is the function that will be bound as a method to an instance of the class. The second argument is the class. The third argument is the name of the method.
<code>&gt;&gt;&gt; class X(object):
...     pass
...
&gt;&gt;&gt; f = types.MethodType(lambda self: self.foo, X, 'foo')
&gt;&gt;&gt; f
&lt;unbound method X.&lt;lambda&gt;&gt;
&gt;&gt;&gt; x = X()
&gt;&gt;&gt; x.foo = 'bar'
&gt;&gt;&gt; x.foo
'bar'
&gt;&gt;&gt; f(x)
'bar'
</code>

