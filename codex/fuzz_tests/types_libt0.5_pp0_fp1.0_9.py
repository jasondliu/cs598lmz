import types
types.MethodType(lambda self: self.x, x)
</code>
You can also use <code>types.FunctionType</code> to create a function that is bound to a particular instance:
<code>&gt;&gt;&gt; import types
&gt;&gt;&gt; f = types.FunctionType(lambda self: self.x, x)
&gt;&gt;&gt; f()
'foo'
</code>

