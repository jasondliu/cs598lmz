import types
types.ModuleType
</code>
However, <code>types.ModuleType</code> is apparently not a valid argument to <code>type()</code>:
<code>&gt;&gt;&gt; type(types.ModuleType)
&lt;type 'type'&gt;
</code>
So, is there any way to do what I'm asking?


A:

You can't create a module with <code>type()</code>. If you want to create a module, you can use the built-in <code>module()</code> function:
<code>&gt;&gt;&gt; module = types.ModuleType('mymodule')
&gt;&gt;&gt; module.__name__
'mymodule'
&gt;&gt;&gt; module.__dict__
{'__name__': 'mymodule', '__doc__': None}
</code>

