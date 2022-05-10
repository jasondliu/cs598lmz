import types
types.ModuleType.__init__
</code>
The <code>object</code> class does not have <code>__init__</code>, but its <code>type</code> does. So the above code is equivalent to:
<code>types.ModuleType.__init__ = lambda *args, **kwargs: None
</code>
The above code works because <code>types.ModuleType</code> is a <code>type</code> object and not just a normal class:
<code>&gt;&gt;&gt; type(types.ModuleType)
&lt;class 'type'&gt;
</code>

